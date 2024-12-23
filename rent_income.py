from fastapi import FastAPI, HTTPException, Query, Body, Depends, Path
from pydantic import BaseModel
from typing import Dict
from db import get_db
import logging
from fastapi.middleware.cors import CORSMiddleware
import schemas, crud, models
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy import func


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


@app.get("/rent_income_details/{etin}/{id}")
def read_rent_details_income(etin: str, id : int, db: Session = Depends(get_db)):
    return crud.get_rent_details_income(db, etin= etin, id = id)
    

@app.get("/rent_income_details/")
def read_rent_details_incomes(skip: int = Query(...), limit: int = Query(...), db: Session = Depends(get_db)):
    items = crud.get_rent_details_incomes(db, skip=skip, limit=limit)
    return items

@app.get("/rent_income_master/{etin}")
def read_rent_master_income(etin: str, db: Session = Depends(get_db)):
    return crud.get_rent_master_income(db, etin= etin)
    

@app.get("/rent_income_master/")
def read_rent_master_incomes(skip: int = Query(...), limit: int = Query(...), db: Session = Depends(get_db)):
    items = crud.get_rent_master_incomes(db, skip=skip, limit=limit)
    return items

@app.get("/rent_income_summary/{etin}")
def read_rent_summary_income(etin: str, db: Session = Depends(get_db)):
    return crud.get_rent_summary_income(db, etin= etin)
    

@app.get("/rent_income_summary/")
def read_rent_summary_incomes(skip: int = Query(...), limit: int = Query(...), db: Session = Depends(get_db)):
    items = crud.get_rent_summary_incomes(db, skip=skip, limit=limit)
    return items




@app.post("/rent_income/")
def create_rent_details_income(
    rent_income_master: schemas.Rent_Income_Master = Body(...),
    rent_income_details: List[schemas.Rent_Income_Details] = Body(...),
    etin: str = Body(...),
    db: Session = Depends(get_db)
):
    # Validate rent income details
    if len(rent_income_details) != rent_income_master.total_flats:
        return {"error": f"Expected {rent_income_master.total_flats} rent income details, but received {len(rent_income_details)}."}

    # Check for existing master
    master = db.query(models.RentIncomeMaster).filter(
        models.RentIncomeMaster.etin == etin,
        models.RentIncomeMaster.asset_address == rent_income_master.asset_address,
        models.RentIncomeMaster.area_type == rent_income_master.area_type
    ).first()

    if not master:
        # Create master if it doesn't exist
        master = crud.create_rent_master_income(db=db, rent_income_master=rent_income_master, etin=etin)

    else:
        # Update the master if it exists
        crud.update_rent_master_income(db=db, etin=etin, updated_data=rent_income_master)

    for details in rent_income_details:
        # Check if details exist for the current master
        existing_detail = db.query(models.RentIncomeDetails).filter(
            models.RentIncomeDetails.etin == etin,
            models.RentIncomeDetails.master_id == master.id,
            models.RentIncomeDetails.space_type == details.space_type
        ).first()

        if existing_detail:
            # Update existing details
            crud.update_rent_details_income(db=db, etin=etin, updated_data=details)
        else:
            # Create new details under the existing master
            crud.create_rent_details_income(db=db, rent_income_details=details, etin=etin, master_id= master.id)

    # Recalculate and update totals and allowances
    all_details = db.query(models.RentIncomeDetails).filter(
        models.RentIncomeDetails.etin == etin,
        models.RentIncomeDetails.master_id == master.id
    ).all()

    # Initialize totals
    # gross_total_rent_month = 0
    # gross_total_vacancy_month = 0
    # rent_month = 0
    # month_total = 0
    
    gross_total_rent_month = 0
    gross_total_vacancy_month = 0
    master.rent_taken = 0
    master.total_income = 0
    master.yearly_value = 0
    master.total_adjusted_advance = 0
    master.other_charge = 0
    rent_month = 0
    month_total = 0

    area_rate = 0.25 if rent_income_master.area_type.lower() == "residential" else 0.3 if rent_income_master.area_type.lower() == "business" else 0

    for details in all_details:
        # Calculate rent months
        total_rent_month = (
            12 if details.live_ownself.lower() == "yes" or details.all_month.lower() == "yes"
            else sum(1 for month in [
                details.january, details.february, details.march, details.april,
                details.may, details.june, details.july, details.august,
                details.september, details.october, details.november, details.december
            ] if month.lower() == "yes")
        )
        if details.live_ownself.lower() == "no":
            rent_month += sum(1 for month in [
                details.january, details.february, details.march, details.april,
                details.may, details.june, details.july, details.august,
                details.september, details.october, details.november, details.december
            ] if month.lower() == "yes")

        # Update details calculations
        details.total_rent = details.monthly_rent * 12
        details.total_rent_received = details.monthly_rent * total_rent_month
        details.total_vacancy_month = 12 - total_rent_month
        details.adjusted_advance = details.advance - details.adjusted_rent
        
        print("total_rent",details.total_rent)
        print("total_rent_received",details.total_rent_received)
        print("total_vacancy_month",details.total_vacancy_month)
        print("adjusted_advance",details.adjusted_advance)
        

        gross_total_rent_month += total_rent_month
        gross_total_vacancy_month += details.total_vacancy_month

        print("gross_total_rent_month",gross_total_rent_month)
        print("gross_total_vacancy_month",gross_total_vacancy_month)
        
        # Update master totals
        master.rent_taken += details.monthly_rent * 12
        master.total_income += (details.monthly_rent * total_rent_month) + (details.monthly_service_charge * total_rent_month) + master.other_taken_rent
        master.yearly_value += details.monthly_rent * 12
        master.total_adjusted_advance += details.adjusted_advance
        master.other_charge += (details.monthly_service_charge * total_rent_month)
        master.vacancy_allowance += details.total_vacancy_month * details.monthly_rent
        
        print("total income",master.total_income)
        print("vacancy_allowance",master.vacancy_allowance)
        print("other_taken_rent",master.other_taken_rent)

    # Calculate allowances
    
    master.total_flats = db.query(models.RentIncomeDetails).join(
    models.RentIncomeMaster, models.RentIncomeMaster.id == models.RentIncomeDetails.master_id
    ).filter(
        models.RentIncomeMaster.etin == etin,
        models.RentIncomeMaster.area_type == master.area_type
    ).count()
    
    
    month_total = master.total_flats * 12
    
    print(master.total_flats)
    
    print(rent_month)    
    print(month_total)
    
    ratio = rent_month / month_total
    
    print(ratio)

    master.insurance_premium_paid_allowable = master.insurance_premium_paid_actual * ratio
    master.interest_on_repaid_loans_allowable = master.interest_on_repaid_loans_actual * ratio
    master.land_revenue_allowable = master.land_revenue_actual * ratio
    master.municipal_or_local_tax_allowable = master.municipal_or_local_tax_actual * ratio
    master.receipt_of_repairs_allowable = master.total_income * area_rate * ratio

    # Final calculations
    if master.receipt_of_repairs_actual > master.receipt_of_repairs_allowable:
        master.special_income = 0
        master.net_income = master.total_income - master.receipt_of_repairs_allowable
    else:
        master.special_income = master.receipt_of_repairs_allowable - master.receipt_of_repairs_actual
        master.net_income = master.total_income - master.receipt_of_repairs_actual

    master.total_expense = (
        master.insurance_premium_paid_allowable +
        master.interest_on_repaid_loans_allowable +
        master.land_revenue_allowable +
        master.municipal_or_local_tax_allowable +
        master.receipt_of_repairs_allowable
    )

    master.net_income = master.total_income - master.total_expense + master.special_income

    # Commit changes
    db.commit()

    return {
        "master": crud.get_rent_master_income(db, etin),
        "details": crud.get_rent_detail_income(db, etin)
    }



# @app.post("/rent_income/")
# def create_rent_details_income(
#     rent_income_master: schemas.Rent_Income_Master = Body(...),
#     rent_income_details: List[schemas.Rent_Income_Details] = Body(...),
#     etin: str = Body(...),
#     db: Session = Depends(get_db)
# ):
#     # Validate rent income details
#     if len(rent_income_details) != rent_income_master.total_flats:
#         return {"error": f"Expected {rent_income_master.total_flats} rent income details, but received {len(rent_income_details)}."}

#     # Check if master exists
#     master = db.query(models.RentIncomeMaster).filter(
#         models.RentIncomeMaster.etin == etin,
#         models.RentIncomeMaster.asset_address == rent_income_master.asset_address,
#         models.RentIncomeMaster.area_type == rent_income_master.area_type
#     ).first()

#     if not master:
#         # Create master if it doesn't exist
#         master = crud.create_rent_master_income(db=db, rent_income_master=rent_income_master, etin=etin)

#     for details in rent_income_details:
#         # Check if details exist for the current master and space type
#         existing_detail = db.query(models.RentIncomeDetails).filter(
#             models.RentIncomeDetails.etin == etin,
#             models.RentIncomeDetails.master_id == master.id,
#             models.RentIncomeDetails.space_type == details.space_type
#         ).first()

#         if existing_detail:
#             # Update existing details
#             crud.update_rent_details_income(db=db, etin=etin, updated_data=details)
#         else:
#             # Create new details if space type does not exist for the master
#             crud.create_rent_details_income(db=db, rent_income_details=details, etin=etin, master_id=master.id)

#     # Recalculate and update totals and allowances for the current master
#     all_details = db.query(models.RentIncomeDetails).filter(
#         models.RentIncomeDetails.etin == etin,
#         models.RentIncomeDetails.master_id == master.id
#     ).all()

#     # Initialize totals
#     # gross_total_rent_month = 0
#     # gross_total_vacancy_month = 0
#     # rent_month = 0
#     # rent_month_total = 0

#     gross_total_rent_month = 0
#     gross_total_vacancy_month = 0
#     master.rent_taken = 0
#     master.total_income = 0
#     master.yearly_value = 0
#     master.total_adjusted_advance = 0
#     master.other_charge = 0
#     master.total_expense = 0 
#     master.net_income = 0
#     rent_month = 0
#     rent_month_total = 0
#     master.insurance_premium_paid_allowable = 0
#     master.interest_on_repaid_loans_allowable = 0
#     master.land_revenue_allowable = 0
#     master.municipal_or_local_tax_allowable = 0
#     master.receipt_of_repairs_allowable = 0
    

#     area_rate = 0.25 if rent_income_master.area_type.lower() == "residential" else 0.3 if rent_income_master.area_type.lower() == "business" else 0

#     for details in all_details:
#         # Calculate rent months
#         total_rent_month = (
#             12 if details.live_ownself.lower() == "yes" or details.all_month.lower() == "yes"
#             else sum(1 for month in [
#                 details.january, details.february, details.march, details.april,
#                 details.may, details.june, details.july, details.august,
#                 details.september, details.october, details.november, details.december
#             ] if month.lower() == "yes")
#         )
#         if details.live_ownself.lower() == "no":
#             rent_month += sum(1 for month in [
#                 details.january, details.february, details.march, details.april,
#                 details.may, details.june, details.july, details.august,
#                 details.september, details.october, details.november, details.december
#             ] if month.lower() == "yes")

#         # Update details calculations
#         details.total_rent = details.monthly_rent * 12
#         details.total_rent_received = details.monthly_rent * total_rent_month
#         details.total_vacancy_month = 12 - total_rent_month
#         details.adjusted_advance = details.advance - details.adjusted_rent

#         gross_total_rent_month += total_rent_month
#         gross_total_vacancy_month += details.total_vacancy_month

#         # Update master totals
#         master.rent_taken += details.monthly_rent * 12
#         master.total_income += (details.monthly_rent * total_rent_month) + (details.monthly_service_charge * total_rent_month) + master.other_taken_rent
#         master.yearly_value += details.monthly_rent * 12
#         master.total_adjusted_advance += details.adjusted_advance
#         master.other_charge += (details.monthly_service_charge * total_rent_month)
#         master.vacancy_allowance += details.total_vacancy_month * details.monthly_rent
#         # income = (details.monthly_rent * total_rent_month) + (details.monthly_service_charge * total_rent_month) + master.other_taken_rent
        
#         # print(income)

#     # Calculate allowances
#     rent_month_total = master.total_flats * 12
#     ratio = rent_month / rent_month_total

#     master.insurance_premium_paid_allowable = master.insurance_premium_paid_actual * ratio
#     master.interest_on_repaid_loans_allowable = master.interest_on_repaid_loans_actual * ratio
#     master.land_revenue_allowable = master.land_revenue_actual * ratio
#     master.municipal_or_local_tax_allowable = master.municipal_or_local_tax_actual * ratio
#     master.receipt_of_repairs_allowable = master.total_income * area_rate * ratio
#     # master.receipt_of_repairs_allowable = income * area_rate * ratio
#     print(master.receipt_of_repairs_allowable)

#     # Final calculations
#     if master.receipt_of_repairs_actual > master.receipt_of_repairs_allowable:
#         master.special_income = 0
#         master.net_income = master.total_income - master.receipt_of_repairs_allowable
#     else:
#         master.special_income = master.receipt_of_repairs_allowable - master.receipt_of_repairs_actual
#         master.net_income = master.total_income - master.receipt_of_repairs_actual

#     master.total_expense = (
#         master.insurance_premium_paid_allowable +
#         master.interest_on_repaid_loans_allowable +
#         master.land_revenue_allowable +
#         master.municipal_or_local_tax_allowable +
#         master.receipt_of_repairs_allowable
#     )

#     master.net_income = master.total_income - master.total_expense + master.special_income

#     # Commit changes
#     db.commit()

#     return {
#         "master": crud.get_rent_master_income(db, etin),
#         "details": crud.get_rent_detail_income(db, etin)
#     }
