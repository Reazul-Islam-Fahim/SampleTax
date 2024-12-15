from fastapi import FastAPI, HTTPException, Query, Body, Depends, Path
from pydantic import BaseModel
from typing import Dict
from db import get_db
import logging
from fastapi.middleware.cors import CORSMiddleware
import schemas, crud, models
from sqlalchemy.orm import Session

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


@app.get("/rent_income_details/{etin}")
def read_rent_details_income(etin: str, db: Session = Depends(get_db)):
    return crud.get_rent_details_income(db, etin= etin)
    

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
    rent_income_details: schemas.Rent_Income_Details = Body(...), 
    rent_income_master : schemas.Rent_Income_Master = Body(...), 
    rent_income_summary : schemas.Rent_Income_Summary = Body(...),
    etin : str = Body(...), db: Session = Depends(get_db)
    ):
    
    crud.create_rent_details_income(db, rent_income_details, etin)
    crud.create_rent_master_income(db, rent_income_master, etin)
    crud.create_rent_summary_income(db, rent_income_summary, etin)
    
    rent_income_details = crud.get_rent_details_income(db, etin = etin)
    
    if(rent_income_details.area_type.lower() == "residential"):
        area_rate = 0.25
    elif(rent_income_details.area_type.lower() == "commercial"):
        area_rate = 0.3
        
        
    if(rent_income_master.live_ownself.lower() == "yes"):
        total_rent_month = 12
    else:
        total_rent_month = 0
        if(rent_income_master.january.lower() == "yes"):
            total_rent_month+=1
        if(rent_income_master.february.lower() == "yes"):
            total_rent_month+=1
        if(rent_income_master.march.lower() == "yes"):
            total_rent_month+=1
        if(rent_income_master.april.lower() == "yes"):
            total_rent_month+=1
        if(rent_income_master.may.lower() == "yes"):
            total_rent_month+=1
        if(rent_income_master.june.lower() == "yes"):
            total_rent_month+=1
        if(rent_income_master.july.lower() == "yes"):
            total_rent_month+=1
        if(rent_income_master.august.lower() == "yes"):
            total_rent_month+=1
        if(rent_income_master.september.lower() == "yes"):
            total_rent_month+=1
        if(rent_income_master.october.lower() == "yes"):
            total_rent_month+=1
        if(rent_income_master.november.lower() == "yes"):
            total_rent_month+=1
        if(rent_income_master.december.lower() == "yes"):
            total_rent_month+=1  
        
    rent_income_master.total_vacancy_month = 12 - total_rent_month
    
    rent_income_details.total_income = (rent_income_master.monthly_rent * total_rent_month) + (rent_income_master.monthly_service_charge * total_rent_month) + rent_income_details.other_taken_rent
    
    rent_income_details.receipt_of_repairs_allowable = rent_income_details.total_income * area_rate
    
    if(rent_income_details.receipt_of_repairs_actual > rent_income_details.receipt_of_repairs_allowable):
        # rent.special_income = rent.receipt_of_repairs_allowable
        rent_income_details.special_income = 0
        rent_income_details.net_income = rent_income_details.total_income - rent_income_details.receipt_of_repairs_allowable
    else:
        rent_income_details.special_income = rent_income_details.receipt_of_repairs_allowable - rent_income_details.receipt_of_repairs_actual
        rent_income_details.net_income = rent_income_details.total_income - rent_income_details.receipt_of_repairs_actual
        
    
    rent_income_details.total_expense = (rent_income_details.insurance_premium_paid_allowable + rent_income_details.interest_on_repaid_loans_allowable + 
                                        rent_income_details.land_revenue_allowable + rent_income_details.municipal_or_local_tax_allowable + rent_income_details.receipt_of_repairs_allowable)
    
    rent_income_details.net_income = rent_income_details.net_income - (rent_income_details.insurance_premium_paid_allowable + rent_income_details.interest_on_repaid_loans_allowable + 
                                                                       rent_income_details.land_revenue_allowable + rent_income_details.municipal_or_local_tax_allowable)
    
    
    
    
     
    
    print(rent_income_details.etin)
    
    return rent_income_details