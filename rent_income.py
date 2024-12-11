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
def create_rent_income(rent_income: schemas.Rent_income = Body(...), etin : str = Body(...), db: Session = Depends(get_db)):
    crud.create_rent_income(db, rent_income, etin= etin)
    
    rent = crud.get_rent_income(db, etin = etin)
    
    
    
    print(rent.etin)
    
    return rent