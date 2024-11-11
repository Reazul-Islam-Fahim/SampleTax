from fastapi import FastAPI, HTTPException, Query, Body
from pydantic import BaseModel
from typing import Dict
from db import get_db
import logging
from fastapi.middleware.cors import CORSMiddleware
import models
from sqlalchemy.orm import Session
from schemas import TaxPayers, PrivateSalary_IncomeRecord, GovSalary_IncomeRecord

app = FastAPI()

# origins = [
#     "https://localhost:8000",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins = origins,
#     allow_credentials = True,
#     allow_methods = ['*'],
#     allow_headers = ['*']
# )



class TableName(BaseModel):
    table_name: str


# Define the input data structure
class IncomeInput(TaxPayers, PrivateSalary_IncomeRecord, GovSalary_IncomeRecord):
    pass

class IncomeCalculator:
    def __init__(self, employment_type, income_data: IncomeInput):
        self.employment_type = employment_type
        self.income_data = income_data
        self.income_from_job = 0

    def calc_income(self):
        if self.employment_type.upper() == "PRIVATE":
            vehicle_facility_provided = self._get_vehicle_facility()
            #other_non_cash = self._get_other_benefits()
            self.income_from_job = (
                self.income_data.basic_salary +
                self.income_data.house_rent_allowance +
                self.income_data.medical_allowance +
                self.income_data.conveyance_allowance +
                self.income_data.festival_bonus +
                self.income_data.rent_free_accommodation +
                self.income_data.accommodation_at_concessional_rate -
                self.income_data.rent_paid_by_taxpayer +
                self.income_data.arrear_salary  +
                self.income_data.education_allowance  +
                self.income_data.entertainment_allowance  +
                self.income_data.employer_contribution_RPF  +
                self.income_data.leave_allowance  +
                self.income_data.other_bonus  +
                self.income_data.overtime_bonus  +
                self.income_data.pension  +
                self.income_data.tada  +
                self.income_data.income_from_employee_share_scheme  +
                self.income_data.others  +
                self.income_data.commission  +
                self.income_data.fee  +
                self.income_data.mohargha_allowance +
                vehicle_facility_provided 
            )
            
            self.income_data.allowances = (
                self.income_data.leave_allowance  +
                self.income_data.other_bonus  +
                self.income_data.overtime_bonus  +
                self.income_data.fee  +
                self.income_data.commission    
            )
            
            
            self.income_data.perquisites = (
                self.income_data.medical_allowance +
                self.income_data.entertainment_allowance  +
                self.income_data.house_rent_allowance +
                self.income_data.accommodation_at_concessional_rate +
                self.income_data.conveyance_allowance +
                self.income_data.mohargha_allowance 
            )
            
            
            return self.income_from_job
            
        else:
            self.income_from_job = (
                self.income_data.basic_salary +
                self.income_data.house_rent_allowance +
                self.income_data.medical_allowance +
                self.income_data.conveyance_allowance +
                self.income_data.festival_bonus +
                self.income_data.arrear_pay +
                self.income_data.special_allowance +
                self.income_data.support_staff_allowance +
                self.income_data.leave_allowance +
                self.income_data.reward +
                self.income_data.overtime + 
                self.income_data.bangla_noboborsho +
                self.income_data.interest_accrued_from_PF +
                self.income_data.lump_grant +
                self.income_data.gratuity +
                self.income_data.others
            )
            
            return self.income_data.basic_salary + self.income_data.festival_bonus

    def _get_vehicle_facility(self):
        vehicle_facility_provided = 0
        if self.income_data.vehicle_facility_months > 0:
            vehicle_facility_provided = self.income_data.vehicle_facility_months * (25000 if self.income_data.is_higher_cc == "Y" else 10000)
        return vehicle_facility_provided

    def _get_other_benefits(self):
        other_non_cash = 0
        if self.income_data.other_non_cash_benefits:
            for value in self.income_data.other_non_cash_benefits.values():
                other_non_cash += value
        return other_non_cash

class TaxLiabilityCalculator:
    def __init__(self, taxable_income):
        self.taxable_income = taxable_income
        self.exemption_limit = 0

    def set_exemption_limit(self, category, num_autistic_children):
        exemptions = {
            1: 350000,
            2: 400000,
            3: 475000,
            4: 500000
        }
        self.exemption_limit = exemptions.get(category, 0) + (num_autistic_children * 50000)

    def calculate_tax(self):
        taxable_income_after_exemption = max(0, self.taxable_income - self.exemption_limit)
        return self._calculate_tax_liability(taxable_income_after_exemption)

    def _calculate_tax_liability(self, taxable_income):
        tax_liability = 0
        slabs = [
            (100000, 0.05),
            (400000, 0.10),
            (500000, 0.15),
            (500000, 0.20),
            (2000000, 0.25),
            (float('inf'), 0.30)
        ]

        for limit, rate in slabs:
            if taxable_income <= 0:
                break
            taxable_amount = min(taxable_income, limit)
            tax_liability += taxable_amount * rate
            taxable_income -= taxable_amount

        return tax_liability


@app.post("/calculate_income/")
async def calculate_income(income_input: IncomeInput = Body(...)):
    

    income_calculator = IncomeCalculator(income_input.is_government, income_input)
    total_income = income_calculator.calc_income()

    taxable_income = total_income - (total_income / 3 if (total_income / 3) < 450000 else 450000)

    tax_calculator = TaxLiabilityCalculator(taxable_income)
    tax_calculator.set_exemption_limit(income_input.category, income_input.num_autistic_children)
    tax_liability = tax_calculator.calculate_tax()

    connection = get_db()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"INSERT INTO {income_input.table_name} (ID, TOTAL_INCOME, TAXABLE_INCOME, TAX_LIABILITY) VALUES (%s %s %s %s)",
                (income_input.id, total_income, taxable_income, tax_liability)
            )
            connection.commit()
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    connection.close()

    return {
        "id": income_input.id,
        "total_income": total_income,
        "taxable_income": taxable_income,
        "tax_liability": tax_liability
    }

@app.get("/get_income_records/")
async def get_income_records(tablename : TableName = Query(...)):
    connection = get_db()
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {tablename.table_name}")
        column_names = [desc[0] for desc in cursor.description]
            
        # Fetch all rows
        rows = cursor.fetchall()

        # Format rows with column names
        data = [dict(zip(column_names, row)) for row in rows]
        
        return {"data": data}

    except Exception as e:
        logging.error(f"Error fetching income records: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    finally:
        cursor.close()
        connection.close()


@app.get("/")
async def hi():
    return {"hello": "Welcome to taxdo"}





