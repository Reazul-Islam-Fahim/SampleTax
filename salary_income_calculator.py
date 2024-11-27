from fastapi import FastAPI, HTTPException, Query, Body, Depends, Path
from pydantic import BaseModel
from typing import Dict
from db import get_db
import logging
from fastapi.middleware.cors import CORSMiddleware
import schemas
from sqlalchemy.orm import Session
import schemas 
import crud,models
from age import calculate_age

app = FastAPI()

origins = [
    "http://192.168.2.33:5173",
    # "https://yourfrontenddomain.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)



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
        self.total_income += vehicle_facility.total
        return self.total_income

    def _calculate_private_income(self):
        return (
            self.salary_data.private_allowances +
            self.salary_data.private_arrear_salary +
            self.salary_data.private_gratuity +
            self.salary_data.private_perquisites +
            self.salary_data.private_receipts_or_additional_receipts_in_lieu_of_salary +
            self.salary_data.private_income_from_employee_share_scheme +
            self.salary_data.private_housing_facility +
            self.salary_data.private_vehicle_facility +
            self.salary_data.private_any_other_benefit_provided_by_the_employer +
            self.salary_data.private_contribution_paid_by_employer_to_recognized_pf+
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





@app.post("/api/calculate_salary_income/")
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
    
    salary_data.private_allowances = allowances.total
    salary_data.private_perquisites = perquisites.total
    salary_data.private_vehicle_facility = vehicle_facility.total
    
    crud.create_salary_income_record(db, salary_data)
    crud.create_allowance(db, allowances, salary_data.etin)
    crud.create_perquisite(db, perquisites, salary_data.etin)
    crud.create_vehicle_falitiy(db, vehicle_facility, salary_data.etin)
        
    
    get_allowance = crud.get_allowance(db, salary_data.etin)
    get_perquisite = crud.get_perquisite(db, salary_data.etin)
    get_vehicle = crud.get_vehicle_falitiy(db, salary_data.etin)
    
    print(get_allowance.total, get_perquisite.total, get_vehicle.total)
    

    # # Save the salary income summary
    exempted_income = total_income - taxable_income
   
    salary_income_summary = schemas.SalaryIncome_Summary(
        total_income=int(total_income),
        exempted_income= int(exempted_income),
        taxable_income=int(taxable_income),
        tax_liability=int(tax_liability)
    )
    
    crud.create_salary_income_summary(db, salary_income_summary, salary_data.etin)

    return {
        "total_income": total_income,
        "exempted_income": exempted_income,
        "taxable_income": taxable_income,
        "tax_liability": tax_liability
    }




@app.put("/salary_income_record/{etin}", response_model=schemas.SalaryIncome_Record)
async def update_salary_income_record_endpoint(
    etin: str,
    updated_salary: schemas.SalaryIncome_Record,
    db: Session = Depends(get_db),
):
    updated_record = crud.update_salary_income_record(db, etin, updated_salary)

    if updated_record is None:
        raise HTTPException(status_code=404, detail="SalaryIncomeRecord not found")
    
    return updated_record




    
@app.get("/api/get_salary_income_record/{etin}")
async def get_income_records(etin : str = Path(...),  db: Session = Depends(get_db)):
    db_item = crud.get_salary_income_record(db, etin = etin)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

    

@app.get("/api/get_salary_income_records/")
async def get_income_records(skip : int = Query(...), limit : int = Query(...),  db: Session = Depends(get_db)):
    return crud.get_salary_income_records(db, skip=skip, limit=limit)


@app.get("/")
async def hi():
    return {"hello": "Welcome to taxdo"}



