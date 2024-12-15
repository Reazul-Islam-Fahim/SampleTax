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


@app.get("/rent_income/{etin}")
def read_rent_income(etin: str, db: Session = Depends(get_db)):
    return crud.get_rent_income(db, etin= etin)
    

@app.get("/rent_income/")
def read_rent_incomes(skip: int = Query(...), limit: int = Query(...), db: Session = Depends(get_db)):
    items = crud.get_rent_incomes(db, skip=skip, limit=limit)
    return items


@app.post("/rent_income/")
def create_rent_details_income(rent_income_dtails: schemas.Rent_Income_Details = Body(...), rent_income_master : schemas.Rent_Income_Master = Body(...), etin : str = Body(...), db: Session = Depends(get_db)):
    crud.create_rent_details_income(db, rent_income_dtails, etin= etin)
    crud.create_rent_master_income(db, rent_income_master, etin= etin)
    
    rent = crud.get_rent_details_income(db, etin = etin)
    
    if(rent.area_type.lower() == "residential"):
        area_rate = 0.25
    elif(rent.area_type.lower() == "commercial"):
        area_rate = 0.3
    
    total_rent_month = 0
    if(rent.january.lower() == "yes"):
        total_rent_month+=1
    if(rent.february.lower() == "yes"):
        total_rent_month+=1
    if(rent.march.lower() == "yes"):
        total_rent_month+=1
    if(rent.april.lower() == "yes"):
        total_rent_month+=1
    if(rent.may.lower() == "yes"):
        total_rent_month+=1
    if(rent.june.lower() == "yes"):
        total_rent_month+=1
    if(rent.july.lower() == "yes"):
        total_rent_month+=1
    if(rent.august.lower() == "yes"):
        total_rent_month+=1
    if(rent.september.lower() == "yes"):
        total_rent_month+=1
    if(rent.october.lower() == "yes"):
        total_rent_month+=1
    if(rent.november.lower() == "yes"):
        total_rent_month+=1
    if(rent.december.lower() == "yes"):
        total_rent_month+=1  
        
    rent.total_vacancy_month = 12 - total_rent_month
    
    rent.total_income = (rent.monthly_rent * total_rent_month) + (rent.monthly_service_charge * total_rent_month) + rent.other_taken_rent
    
    rent.receipt_of_repairs_allowable = rent.total_income * area_rate
    
    if(rent.receipt_of_repairs_actual > rent.receipt_of_repairs_allowable):
        # rent.special_income = rent.receipt_of_repairs_allowable
        rent.special_income = 0
        rent.net_income = rent.total_income - rent.receipt_of_repairs_allowable
    else:
        rent.special_income = rent.receipt_of_repairs_allowable - rent.receipt_of_repairs_actual
        rent.net_income = rent.total_income - rent.receipt_of_repairs_actual
        
    
    rent.total_expense = rent.insurance_premium_paid_allowable + rent.interest_on_repaid_loans_allowable + rent.land_revenue_allowable + rent.municipal_or_local_tax_allowable + rent.receipt_of_repairs_allowable
    
    rent.net_income = rent.net_income - (rent.insurance_premium_paid_allowable + rent.interest_on_repaid_loans_allowable + rent.land_revenue_allowable + rent.municipal_or_local_tax_allowable)
    
     
    
    print(rent.etin)
    
    return rent