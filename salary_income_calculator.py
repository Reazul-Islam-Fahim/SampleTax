from fastapi import FastAPI, HTTPException, Query, Body, Depends, Path
from pydantic import BaseModel
from typing import Dict
from db import get_db
import logging
from fastapi.middleware.cors import CORSMiddleware
import schemas, crud, models
from sqlalchemy.orm import Session 
from age import calculate_age
from tax_slab import _calculate_tax_liability
import logging

logger = logging.getLogger(__name__)

app = FastAPI()

origins = [
    "http://192.168.2.33:5173",
    "http://192.168.2.48",
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
            self.salary_data.gov_special_allowance +
            self.salary_data.gov_medical_allowance +
            self.salary_data.gov_conveyance_allowance +
            self.salary_data.gov_festival_allowance +
            self.salary_data.gov_house_rent_allowance +
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
        return taxable_income_after_exemption




@app.get("/employer_info/{etin}")
def read_employer_info(etin: str, db: Session = Depends(get_db)):
    db_item = crud.get_employer_info(db, etin=etin)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Employer info not found")
    return db_item


@app.put("/employer_info/{etin}")
async def update_employer_info_endpoint(
    etin: str,
    updated_employer_info: schemas.Employer_info,
    db: Session = Depends(get_db),
):
    updated_record = crud.update_employer_info(db, etin, updated_employer_info)
    
    if updated_record is None:
        raise HTTPException(status_code=404, detail="EmployerInfo record not found")
    
    return updated_record


@app.get("/employer_info/")
def read_employer_infos(skip : int = Query(...), limit : int = Query(...), db: Session = Depends(get_db)):
    items = crud.get_employer_infos(db, skip=skip, limit=limit)
    return items

@app.post("/employer_info/")
def create_employer_info_route(employer_info: schemas.Employer_info = Body(...), etin : str = Body(...), db: Session = Depends(get_db)):
    user = crud.get_tax_payer(db, etin)
    return crud.create_employer_info(db=db, employer_info=employer_info, petin= user.etin)



    
@app.get("/salary_income/{etin}/{employer_id}")
async def get_income_records(etin : str = Path(...), employer_id : int = Path(...),  db: Session = Depends(get_db)):
    db_item = crud.get_salary_income_record_with_employer(db, etin = etin, employer_id= employer_id)
    perquisite = crud.get_perquisite(db, etin, employer_id)
    allowance = crud.get_allowance(db, etin, employer_id)
    vehicle = crud.get_vehicle_facilitiy(db, etin, employer_id)

    return {
        "salary_data": db_item,
        "allowances": allowance,
        "perquisites": perquisite,
        "vehicle_facility": vehicle
    }




@app.get("/salary_summary/{etin}")
def read_salary_summary(etin: str, db: Session = Depends(get_db)):
    return crud.get_salary_income_summary(db, etin= etin)
    

@app.get("/tax_slab/")
def read_tax_slab(etin: str, db: Session = Depends(get_db)):
    return crud.get_tax_slab(db, etin= etin)



@app.post("/salary_income/")
def update_salary_income(
    salary_data: schemas.SalaryIncome_Record = Body(...),
    allowances: schemas.Allowance_Details = Body(...),
    perquisites: schemas.Perquisite_Details = Body(...),
    vehicle_facility: schemas.Vehicale_facility_Details = Body(...),
    db: Session = Depends(get_db)
):
    user = crud.get_tax_payer(db, etin=salary_data.etin)

    # Check if user exists and has an employment_type
    if not user or not user.employment_type:
        raise HTTPException(status_code=404, detail="User not found or employment type missing.")

    # Retrieve the employment type from the user object
    employment_type = user.employment_type

    # Calculate age and determine tax category
    age = calculate_age(user.date_of_birth)
    category = determine_category(user, age)

    # Update or create the salary income record for the given employer_info_id
    salary = crud.get_salary_income_record_with_employer(db, salary_data.etin, salary_data.employer_info_id)
    if salary:
        crud.update_salary_income_record(db, salary_data.etin, salary_data)
    else:
        crud.create_salary_income_record(db, salary_data)

    # Fetch all salary records for the given etin
    all_salary_records = crud.get_salary_income_record(db, salary_data.etin)

    # Calculate total income across all employer_info_id
    total_income = 0
    for record in all_salary_records:
        allowances = crud.get_allowance(db, record.etin, record.employer_info_id)
        perquisites = crud.get_perquisite(db, record.etin, record.employer_info_id)
        vehicle_facility = crud.get_vehicle_facilitiy(db, record.etin, record.employer_info_id)
        income_calculator = IncomeCalculator(employment_type, record)
        total_income += income_calculator.calculate_total_income(allowances, perquisites, vehicle_facility)

    # Taxable income
    taxable_income = total_income - min(total_income / 3, 450000)

    # Calculate tax
    tax_calculator = TaxLiabilityCalculator(taxable_income)
    tax_calculator.set_exemption_limit(category, user.num_autistic_children)
    taxable_income_after_exemption = tax_calculator.calculate_taxable_income()
    tax_liability = _calculate_tax_liability(db, user.etin, taxable_income_after_exemption)

    exempted_income = total_income - taxable_income

    # Update or create the summary record
    salary_income_summary = schemas.SalaryIncome_Summary(
        total_income=int(total_income),
        exempted_income=int(exempted_income),
        taxable_income=int(taxable_income),
        tax_liability=int(tax_liability)
    )
    summary = crud.get_salary_income_summary(db, salary_data.etin)
    if summary:
        crud.update_salary_income_summary(db, salary_data.etin, salary_income_summary)
    else:
        crud.create_salary_income_summary(db, salary_income_summary, salary_data.etin)

    return {
        "total_income": total_income,
        "salary_data": salary_data,
        "allowances": allowances,
        "perquisites": perquisites,
        "vehicle_facility": vehicle_facility
    }


