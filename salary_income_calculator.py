from fastapi import FastAPI, HTTPException, Query, Body, Depends, Path
from pydantic import BaseModel
from typing import Dict
from db import get_db
import logging
from fastapi.middleware.cors import CORSMiddleware
import schemas
from sqlalchemy.orm import Session
from schemas import PrivateSalary_IncomeRecord, GovSalary_IncomeRecord
import crud
from age import calculate_age

app = FastAPI()

# origins = [
#     "https://localhost:8000",
#     "https://yourfrontenddomain.com",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins = origins,
#     allow_credentials = True,
#     allow_methods = ['*'],
#     allow_headers = ['*']
# )



class IncomeCalculator:
    def __init__(self, employment_type: str, salary_data: schemas.SalaryIncome_Record):
        self.employment_type = employment_type
        self.salary_data = salary_data
        self.total_income = 0

    def calculate_total_income(self, allowances: schemas.Allowance_Details, perquisites: schemas.Perquisite_Details, vehicle_facility: schemas.Vehicale_facility_Details):
        # Base salary
        self.total_income += self.salary_data.basic_salary

        if self.employment_type.upper() == "PRIVATE":
            self.total_income += self._calculate_private_income()
        elif self.employment_type.upper() == "GOVERNMENT":
            self.total_income += self._calculate_gov_income()
        else:
            raise HTTPException(status_code=400, detail="Invalid employment type.")

        # Include allowances, perquisites, and vehicle facility
        self.total_income += allowances.total
        self.total_income += perquisites.total
        self.total_income += vehicle_facility.no_of_months * (
            vehicle_facility.cost_for_upto_2500
            if vehicle_facility.upto_2500CC.upper() == "YES"
            else vehicle_facility.cost_for_more_than_2500
        )
        return self.total_income

    def _calculate_private_income(self):
        return (
            self.salary_data.private_allowances +
            self.salary_data.private_arrear_salary +
            self.salary_data.private_gratuity +
            self.salary_data.private_perquisites +
            self.salary_data.private_receipts_or_additional_receipts_in_lieu_of_salary_or_wages +
            self.salary_data.private_income_from_employee_share_scheme +
            self.salary_data.private_housing_facility +
            self.salary_data.private_vehicle_facility +
            self.salary_data.private_any_other_benefit_provided_by_the_employer +
            self.salary_data.private_contribution_paid_by_employer_to_recognized_provident_fund +
            self.salary_data.private_others
        )

    def _calculate_gov_income(self):
        return (
            self.salary_data.gov_arrear_pay +
            self.salary_data.gov_festival_allowance +
            self.salary_data.gov_special_allowance +
            self.salary_data.gov_support_staff_allowance +
            self.salary_data.gov_leave_allowance +
            self.salary_data.gov_reward +
            self.salary_data.gov_overtime +
            self.salary_data.gov_bangla_noboborsho +
            self.salary_data.gov_interest_accrued_from_PF +
            self.salary_data.gov_lump_grant +
            self.salary_data.gov_gratuity +
            self.salary_data.gov_others
        )





def determine_category(user, age):
    if user.gender.upper() == "MALE":
        return 1
    elif user.gender.upper() == "FEMALE" or age >= 65:
        return 2
    elif user.gender.upper() == "OTHER" or user.disable.upper() == "YES":
        return 3
    elif user.freedom_fighter.upper() == "YES":
        return 4
    elif user.parent_of_disable.upper() == "YES":
        return 5
    return 1


class TaxLiabilityCalculator:
    def __init__(self, taxable_income: float):
        self.taxable_income = taxable_income
        self.exemption_limit = 0

    def set_exemption_limit(self, category: int, num_autistic_children: int):
        exemptions = {
            1: 350000,
            2: 400000,
            3: 475000,
            4: 500000
        }
        self.exemption_limit = exemptions.get(category, 0) + (num_autistic_children * 50000)

    def calculate_taxable_income(self):
        taxable_income_after_exemption = max(0, self.taxable_income - self.exemption_limit)
        return self._calculate_tax_liability(taxable_income_after_exemption)

    def _calculate_tax_liability(self, taxable_income: float):
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










# class IncomeCalculator:
#     def __init__(self, employment_type, income_data: BaseModel):
#         self.employment_type = employment_type
#         self.income_data = income_data
#         self.income_from_job = 0

#     def calc_income(self):
#         if self.employment_type.upper() == "PRIVATE":
#             return self._calculate_private_income()
#         else:
#             return self._calculate_gov_income()

#     def _calculate_private_income(self):
#         vehicle_facility_provided = self._get_vehicle_facility()
#         self.income_from_job = (
#             self.income_data.basic_salary +
#             self.income_data.house_rent_allowance +
#             self.income_data.medical_allowance +
#             self.income_data.conveyance_allowance +
#             self.income_data.festival_bonus +
#             self.income_data.rent_free_accommodation +
#             self.income_data.accommodation_at_concessional_rate -
#             self.income_data.rent_paid_by_taxpayer +
#             self.income_data.arrear_salary +
#             self.income_data.education_allowance +
#             self.income_data.entertainment_allowance +
#             self.income_data.employer_contribution_RPF +
#             self.income_data.leave_allowance +
#             self.income_data.other_bonus +
#             self.income_data.overtime_bonus +
#             self.income_data.pension +
#             self.income_data.tada +
#             self.income_data.income_from_employee_share_scheme +
#             self.income_data.others +
#             self.income_data.commission +
#             self.income_data.fee +
#             self.income_data.mohargha_allowance +
#             vehicle_facility_provided
#         )
        
#         allowances = (
#             self.income_data.leave_allowance +
#             self.income_data.other_bonus +
#             self.income_data.overtime_bonus +
#             self.income_data.fee +
#             self.income_data.commission
#         )

#         perquisites = (
#             self.income_data.medical_allowance +
#             self.income_data.entertainment_allowance +
#             self.income_data.house_rent_allowance +
#             self.income_data.accommodation_at_concessional_rate +
#             self.income_data.conveyance_allowance +
#             self.income_data.mohargha_allowance
#         )

#         return [self.income_from_job, allowances, perquisites]

#     def _calculate_gov_income(self):
#         self.income_from_job = (
#             self.income_data.basic_salary +
#             self.income_data.house_rent_allowance +
#             self.income_data.medical_allowance +
#             self.income_data.conveyance_allowance +
#             self.income_data.festival_allowance +
#             self.income_data.arrear_pay +
#             self.income_data.special_allowance +
#             self.income_data.support_staff_allowance +
#             self.income_data.leave_allowance +
#             self.income_data.reward +
#             self.income_data.overtime +
#             self.income_data.bangla_noboborsho +
#             self.income_data.interest_accrued_from_PF +
#             self.income_data.lump_grant +
#             self.income_data.gratuity +
#             self.income_data.others
#         )
        
#         tax_approved_income = self.income_data.basic_salary + self.income_data.festival_allowance
#         return [self.income_from_job, tax_approved_income]

#     def _get_vehicle_facility(self):
#         vehicle_facility_provided = 0
#         if hasattr(self.income_data, 'vehicle_facility_months') and self.income_data.vehicle_facility_months > 0:
#             vehicle_facility_provided = self.income_data.vehicle_facility_months * (
#                 25000 if self.income_data.is_higher_cc == "Y" else 10000)
#         return vehicle_facility_provided



# class TaxLiabilityCalculator:
#     def __init__(self, taxable_income):
#         self.taxable_income = taxable_income
#         self.exemption_limit = 0

#     def set_exemption_limit(self, category, num_autistic_children):
#         exemptions = {
#             1: 350000,
#             2: 400000,
#             3: 475000,
#             4: 500000
#         }
#         self.exemption_limit = exemptions.get(category, 0) + (num_autistic_children * 50000)

#     def calculate_tax(self):
#         taxable_income_after_exemption = max(0, self.taxable_income - self.exemption_limit)
#         return self._calculate_tax_liability(taxable_income_after_exemption)

#     def _calculate_tax_liability(self, taxable_income):
#         tax_liability = 0
#         slabs = [
#             (100000, 0.05),
#             (400000, 0.10),
#             (500000, 0.15),
#             (500000, 0.20),
#             (2000000, 0.25),
#             (float('inf'), 0.30)
#         ]

#         for limit, rate in slabs:
#             if taxable_income <= 0:
#                 break
#             taxable_amount = min(taxable_income, limit)
#             tax_liability += taxable_amount * rate
#             taxable_income -= taxable_amount

#         return tax_liability
    
    
# @app.post("/calculate_private_salary_income/")
# async def calculate_private_income(
#     income_input: PrivateSalary_IncomeRecord = Body(...), 
#     etin: str = Body(...),
#     db: Session = Depends(get_db)
# ):
#     user = crud.get_tax_payer(db, etin = etin)
    
#     crud.create_private_salary_income_record(db, income_input)
    
#     # Calculate age and determine category
#     age = calculate_age(user.date_of_birth)
#     category = 1  # Default category
#     if user.gender.upper() == "MALE":
#         category = 1
#     elif user.gender.upper() == "FEMALE" or age >= 65:
#         category = 2
#     elif user.gender.upper() == "OTHER" or user.disable.upper() == "YES":
#         category = 3
#     elif user.freedom_fighter.upper() == "YES":
#         category = 4
#     elif user.parent_of_disable.upper() == "YES":
#         category = 5

#     # Use the private-sector income calculator
#     income_calculator = IncomeCalculator("PRIVATE", income_input)
#     total_income = income_calculator.calc_income()

#     taxable_income = total_income[0] - (total_income[0] / 3 if (total_income[0] / 3) < 450000 else 450000)

#     tax_calculator = TaxLiabilityCalculator(taxable_income)
#     tax_calculator.set_exemption_limit(category, user.num_autistic_children)
#     tax_liability = tax_calculator.calculate_tax()

#     exempted_income = total_income[0] - taxable_income

#     salary_income_summary = schemas.SalaryIncome_Summary(
#         etin=user.etin,
#         total_income=total_income[0],
#         exempted_income=exempted_income,
#         taxable_income=taxable_income,
#         tax_liability=tax_liability
#     )

#     db_salary_income_summary = crud.create_salary_income_summary(db, salary_income_summary)

#     return db_salary_income_summary


@app.post("/calculate_salary_income/")
async def calculate_salary_income(
    salary_data: schemas.SalaryIncome_Record = Body(...),
    allowances: schemas.Allowance_Details = Body(...),
    perquisites: schemas.Perquisite_Details = Body(...),
    vehicle_facility: schemas.Vehicale_facility_Details = Body(...),
    db: Session = Depends(get_db)
):
    # Retrieve user details using the ETIN from the salary_data
    user = crud.get_tax_payer(db, etin=salary_data.etin)

    # Check if user exists and has an employment_type
    if not user or not user.employment_type:
        raise HTTPException(status_code=404, detail="User not found or employment type missing.")

    # Retrieve the employment type from the user object
    employment_type = user.employment_type

    # Calculate age and determine tax category
    age = calculate_age(user.date_of_birth)
    category = determine_category(user, age)

    # Calculate income
    income_calculator = IncomeCalculator(employment_type, salary_data)
    total_income = income_calculator.calculate_total_income(allowances, perquisites, vehicle_facility)

    # Taxable income
    taxable_income = total_income - min(total_income / 3, 450000)

    # Calculate tax
    tax_calculator = TaxLiabilityCalculator(taxable_income)
    tax_calculator.set_exemption_limit(category, user.num_autistic_children)
    tax_liability = tax_calculator.calculate_taxable_income()

    # Save the salary income summary
    exempted_income = total_income - taxable_income
    salary_income_summary = schemas.SalaryIncome_Summary(
        etin=salary_data.etin,
        total_income=total_income,
        exempted_income=exempted_income,
        taxable_income=taxable_income,
        tax_liability=tax_liability
    )
    crud.create_salary_income_summary(db, salary_income_summary)

    return {
        "total_income": total_income,
        "exempted_income": exempted_income,
        "taxable_income": taxable_income,
        "tax_liability": tax_liability
    }




    
@app.get("/get_salary_income_record/{etin}")
async def get_income_records(etin : str = Path(...),  db: Session = Depends(get_db)):
    db_item = crud.get_salary_income_summary(db, etin = etin)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

    

@app.get("/get_salary_income_records/")
async def get_income_records(skip : int = Query(...), limit : int = Query(...),  db: Session = Depends(get_db)):
    return crud.get_salary_income_summarys(db, skip=skip, limit=limit)


@app.get("/")
async def hi():
    return {"hello": "Welcome to taxdo"}



