from fastapi import FastAPI, HTTPException, Query, Body, Depends, Path
from pydantic import BaseModel
from typing import Dict
from db import get_db
import logging
from fastapi.middleware.cors import CORSMiddleware
import schemas, crud, models
from sqlalchemy.orm import Session
from typing import List


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



# @app.post("/rent_income/")
# def create_rent_details_income(
#     rent_income_master: schemas.Rent_Income_Master = Body(...),
#     rent_income_details: List[schemas.Rent_Income_Details] = Body(...),
#     etin: str = Body(...),
#     db: Session = Depends(get_db)
# ):
#     # Check that the number of rent income details matches total_flats_on_rent
#     if len(rent_income_details) != rent_income_master.total_flats:
#         return {"error": f"Expected {rent_income_master.total_flats} rent income details, but received {len(rent_income_details)}."}

#     master = db.query(models.RentIncomeMaster).filter(
#         models.RentIncomeMaster.etin == etin,
#         models.RentIncomeMaster.asset_address == rent_income_master.asset_address,
#         models.RentIncomeMaster.area_type == rent_income_master.area_type
#     ).first()
#     if not master:
#         print ("error! Master record not found. Please ensure the data is correct or create the master record first.")


#     if master:
#         crud.update_rent_master_income(db = db, etin = etin, updated_data = rent_income_master)
#     else:
#         crud.create_rent_master_income(db = db, rent_income_master = rent_income_master, etin = etin)
        

#     if rent_income_master.area_type.lower() == "residential":
#         area_rate = 0.25
#     elif rent_income_master.area_type.lower() == "business":
#         area_rate = 0.3
#     else:
#         area_rate = 0  # Default case if the area type is not recognized


#     # Now handle RentIncomeDetails
#     total_rent_month = 0
#     gross_total_vacancy_month = 0
#     gross_total_rent_month = 0
    
    
#     for details in rent_income_details:
#         # Check if RentIncomeDetails entry exists for given space_type
#         rent_details = db.query(models.RentIncomeDetails).filter(
#             models.RentIncomeDetails.etin == etin,
#             models.RentIncomeDetails.space_type == details.space_type
#         ).first()

#         if rent_details:
#             crud.update_rent_details_income(db = db, etin = etin, updated_data = details)
#         else:
#             crud.create_rent_details_income(db = db, rent_income_details = details, etin = etin)


#     # Determine the area rate based on area type
#     # if rent_income_master.area_type.lower() == "residential":
#     #     area_rate = 0.25
#     # elif rent_income_master.area_type.lower() == "business":
#     #     area_rate = 0.3
#     # else:
#     #     area_rate = 0  # Default case if the area type is not recognized

#     # total_rent_month = 0
#     # gross_total_vacancy_month = 0
#     # gross_total_rent_month = 0

#     # Process each rent income detail
#     # for i, details in enumerate(rent_income_details):
#     #     rent_details = crud.create_rent_details_income(db, details, etin)

#     #     if rent_details is None:
#     #         # Log the error or return a message indicating that the details were not created
#     #         print(f"Error: Rent details for etin {etin} were not created.")
#     #         return {"error": "Rent details could not be created."}

#     #     # Fetch the rent details using the generated rent_details ID
#     #     details = crud.get_rent_details_income(db, etin, rent_details.id)

#         # Calculate rent month values
#         if details.live_ownself.lower() == "yes" or details.all_month.lower() == "yes":
#             total_rent_month = 12
            
            
            
#         else:
#             months = [
#                 details.january, details.february, details.march, details.april,
#                 details.may, details.june, details.july, details.august,
#                 details.september, details.october, details.november, details.december
#             ]
#             # Count rented months where the month value is 'yes'
#             total_rent_month = sum(1 for month in months if month.lower() == "yes")

#         # Calculate rent-related values for each rent income detail
#         details.total_rent = details.monthly_rent * 12
#         details.total_rent_received = details.monthly_rent * total_rent_month
#         details.total_vacancy_month = 12 - total_rent_month
#         gross_total_rent_month += total_rent_month
#         gross_total_vacancy_month += details.total_vacancy_month

#         # Update master values based on the rent details
#         master.rent_taken += details.monthly_rent * 12
#         master.total_income += ((details.monthly_rent * total_rent_month) + \
#                                (details.monthly_service_charge * total_rent_month) + master.other_taken_rent)
#         master.yearly_value += details.monthly_rent * 12
#         details.adjusted_advance = details.advance - details.adjusted_rent
#         master.total_adjusted_advance += details.adjusted_advance

#     # Calculate ratio for allowances
#     ratio = (master.total_flats_on_rent / master.total_flats)
    
#     master.receipt_of_repairs_allowable = (ratio * master.total_income * area_rate)
#     print(f"receipt_of_repairs_allowable: {master.receipt_of_repairs_allowable}")
    
#     insurance_premium_paid_allowable_monthly =0
#     interest_on_repaid_loans_actual_monthly =0
#     land_revenue_actual_monthly =0
#     municipal_or_local_tax_actual_monthly =0
#     receipt_of_repairs_allowable_monthly =0
    
    
#     if (gross_total_vacancy_month != 0):
#         insurance_premium_paid_allowable_monthly = master.insurance_premium_paid_actual / (master.total_flats * 12)
#         interest_on_repaid_loans_actual_monthly = master.interest_on_repaid_loans_actual / (master.total_flats * 12)
#         land_revenue_actual_monthly = master.land_revenue_actual  / (master.total_flats * 12)
#         municipal_or_local_tax_actual_monthly = master.municipal_or_local_tax_actual / (master.total_flats * 12)
#         receipt_of_repairs_allowable_monthly = (master.total_income * area_rate) / (master.total_flats * 12)
        

#     master.vacancy_allowance = gross_total_vacancy_month * details.monthly_rent
#     master.insurance_premium_paid_allowable = (ratio * master.insurance_premium_paid_actual) - (insurance_premium_paid_allowable_monthly * gross_total_vacancy_month)
#     master.interest_on_repaid_loans_allowable = (ratio * master.interest_on_repaid_loans_actual) - (interest_on_repaid_loans_actual_monthly * gross_total_vacancy_month)
#     master.land_revenue_allowable = (ratio * master.land_revenue_actual) - (land_revenue_actual_monthly * gross_total_vacancy_month)
#     master.municipal_or_local_tax_allowable = (ratio * master.municipal_or_local_tax_actual) - (municipal_or_local_tax_actual_monthly * gross_total_vacancy_month)
#     master.receipt_of_repairs_allowable = master.receipt_of_repairs_allowable - (receipt_of_repairs_allowable_monthly * gross_total_vacancy_month)
    
#     print(f"total_income: {master.total_income}")
#     print(f"area_rate: {area_rate}")
#     print(f"ratio: {ratio}")
#     print(f"receipt_of_repairs_actual_monthly: {receipt_of_repairs_allowable_monthly}")
#     print(f"gross_total_vacancy_month: {gross_total_vacancy_month}")
#     print(f"receipt_of_repairs_allowable: {master.receipt_of_repairs_allowable}")

#     # Special income and net income calculations
#     if master.receipt_of_repairs_actual > master.receipt_of_repairs_allowable:
#         master.special_income = 0
#         master.net_income = master.total_income - master.receipt_of_repairs_allowable
#     else:
#         master.special_income = master.receipt_of_repairs_allowable - master.receipt_of_repairs_actual
#         master.net_income = master.total_income - master.receipt_of_repairs_actual

#     # Total expense calculation
#     master.total_expense = (
#         master.insurance_premium_paid_allowable +
#         master.interest_on_repaid_loans_allowable +
#         master.land_revenue_allowable +
#         master.municipal_or_local_tax_allowable +
#         master.receipt_of_repairs_allowable
#     )

#     master.net_income = master.total_income - master.total_expense + master.special_income

#     # Commit all changes to the database
#     db.commit()

#     return {
#         'master' : crud.get_rent_master_income(db, etin),
#         'details' : crud.get_rent_detail_income(db, etin)
#     }




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

    # Check or create master record
    master = db.query(models.RentIncomeMaster).filter(
        models.RentIncomeMaster.etin == etin,
        models.RentIncomeMaster.asset_address == rent_income_master.asset_address,
        models.RentIncomeMaster.area_type == rent_income_master.area_type
    ).first()

    if not master:
        # Create the master if it does not exist
        master = crud.create_rent_master_income(db=db, rent_income_master=rent_income_master, etin=etin)

    # Update master if it exists
    crud.update_rent_master_income(db=db, etin=etin, updated_data=rent_income_master)

    # Add or update rent income details
    for details in rent_income_details:
        rent_details = db.query(models.RentIncomeDetails).filter(
            models.RentIncomeDetails.etin == etin,
            models.RentIncomeDetails.space_type == details.space_type
        ).first()

        if rent_details:
            crud.update_rent_details_income(db=db, etin=etin, updated_data=details)
        else:
            crud.create_rent_details_income(db=db, rent_income_details=details, etin=etin)

    # Fetch all details for the given etin
    all_details = db.query(models.RentIncomeDetails).filter(
        models.RentIncomeDetails.etin == etin
    ).all()

    # Recalculate totals and allowances based on all details
    gross_total_rent_month = 0
    gross_total_vacancy_month = 0
    master.rent_taken = 0
    master.total_income = 0
    master.yearly_value = 0
    master.total_adjusted_advance = 0
    master.other_charge = 0

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

        # Update details calculations
        details.total_rent = details.monthly_rent * 12
        details.total_rent_received = details.monthly_rent * total_rent_month
        details.total_vacancy_month = 12 - total_rent_month
        details.adjusted_advance = details.advance - details.adjusted_rent

        gross_total_rent_month += total_rent_month
        gross_total_vacancy_month += details.total_vacancy_month

        # Update master based on details
        master.rent_taken += details.monthly_rent * 12
        master.total_income += (details.monthly_rent * total_rent_month) + (details.monthly_service_charge * total_rent_month) + master.other_taken_rent
        master.yearly_value += details.monthly_rent * 12
        master.total_adjusted_advance += details.adjusted_advance
        master.other_charge += (details.monthly_service_charge * total_rent_month)
        
        master.vacancy_allowance += details.total_vacancy_month * details.monthly_rent

    # Calculate allowances
    ratio = master.total_flats_on_rent / master.total_flats
    master.receipt_of_repairs_allowable = ratio * master.total_income * area_rate

    # Adjust allowances for vacancy
    if gross_total_vacancy_month != 0:
        allowance_factors = {
            "insurance_premium_paid": master.insurance_premium_paid_actual / (master.total_flats * 12),
            "interest_on_repaid_loans": master.interest_on_repaid_loans_actual / (master.total_flats * 12),
            "land_revenue": master.land_revenue_actual / (master.total_flats * 12),
            "municipal_or_local_tax": master.municipal_or_local_tax_actual / (master.total_flats * 12),
            "receipt_of_repairs": (master.total_income * area_rate) / (master.total_flats * 12),
        }

        # master.vacancy_allowance = gross_total_vacancy_month * all_details[0].monthly_rent
        master.insurance_premium_paid_allowable = (ratio * master.insurance_premium_paid_actual) - (allowance_factors["insurance_premium_paid"] * gross_total_vacancy_month)
        master.interest_on_repaid_loans_allowable = (ratio * master.interest_on_repaid_loans_actual) - (allowance_factors["interest_on_repaid_loans"] * gross_total_vacancy_month)
        master.land_revenue_allowable = (ratio * master.land_revenue_actual) - (allowance_factors["land_revenue"] * gross_total_vacancy_month)
        master.municipal_or_local_tax_allowable = (ratio * master.municipal_or_local_tax_actual) - (allowance_factors["municipal_or_local_tax"] * gross_total_vacancy_month)
        master.receipt_of_repairs_allowable -= allowance_factors["receipt_of_repairs"] * gross_total_vacancy_month


        print(f"receipt_of_repairs_allowable: {master.receipt_of_repairs_allowable}")

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
