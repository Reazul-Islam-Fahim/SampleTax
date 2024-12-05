
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

@app.get("/financial_asset_income/{etin}", response_model=schemas.Financial_Asset_Income)
def read_financial_asset_income(etin: str, db: Session = Depends(get_db)):
    db_item = crud.get_financial_asset_income(db, etin= etin)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.get("/financial_asset_income/", response_model=list[schemas.Financial_Asset_Income])
def read_financial_asset_incomes(skip: int = Query(...), limit: int = Query(...), db: Session = Depends(get_db)):
    items = crud.get_financial_asset_incomes(db, skip=skip, limit=limit)
    return items


@app.post("/financial_asset_income/", response_model=schemas.Financial_Asset_Income)
def create_financial_asset_income(financial_asset_income: schemas.Financial_Asset_Income = Body(...), etin: str = Body(...), db: Session = Depends(get_db)): 
    crud.create_financial_asset_income(db=db, financial_asset_income=financial_asset_income, petin=etin)
    
    financial_asset = crud.get_financial_asset_income(db, etin)
        
    financial_asset_record = (
            db.query(models.FinancialAssetIncome)
            .filter(models.FinancialAssetIncome.etin == financial_asset.etin)
            .first()
        )
    
    financial_asset_record.total_gross_income = (
            financial_asset_record.total_net_income + 
            financial_asset_record.total_tax_deduction_at_source + 
            financial_asset_record.reduced_tax_rate_securities_net_income + 
            financial_asset_record.reduced_tax_rate_securities_tax_deduction_at_source + 
            financial_asset_record.income_other_resources_net_income + 
            financial_asset_record.income_other_resources_tax_deduction_at_source
            )
    
    financial_asset_record.total_gross_expense = (
            financial_asset_record.total_interest_on_loans + 
            financial_asset_record.total_allowable_expenditure + 
            financial_asset_record.reduced_tax_rate_securities_interest_on_loans + 
            financial_asset_record.reduced_tax_rate_securities_allowable_expenditure + 
            financial_asset_record.income_other_resources_interest_on_loans + 
            financial_asset_record.income_other_resources_allowable_expenditure
            )
        
    financial_asset_record.total_gross_exampted = (
        financial_asset_record.us_dollar_investment_bonds_net_income + 
        financial_asset_record.euro_premium_bonds_net_income + 
        financial_asset_record.pound_sterling_premium_bonds_net_income + 
        financial_asset_record.us_dollar_premium_bonds_net_income + 
        financial_asset_record.wage_earners_development_bonds_net_income + 
        financial_asset_record.euro_investment_bonds_net_income
        )
    
    financial_asset_record.total_gross_taxable = (
        financial_asset_record.total_taxable + 
        financial_asset_record.reduced_tax_rate_securities_taxable + 
        financial_asset_record.income_other_resources_taxable
    )
    
    return financial_asset_record
    

@app.put("/financial_asset_income/{etin}", response_model=schemas.Financial_Asset_Income)
async def update_financial_asset_income(etin: str, financial_asset_income: schemas.Financial_Asset_Income, db: Session = Depends(get_db)):
    updated_record = crud.update_financial_asset_income(db, financial_asset_income=financial_asset_income, petin = etin)
    if updated_record is None:
        raise HTTPException(status_code=404, detail="Financial asset record not found")
    return updated_record


@app.post("/financial_asset_income/", response_model=schemas.Financial_Asset_Income)
def create_financial_asset_income(financial_asset_income: schemas.Financial_Asset_Income = Body(...), etin: str = Body(...), db: Session = Depends(get_db)): 
    db_item = crud.get_financial_asset_income(db, etin= etin)
    if db_item is None:
        return crud.create_financial_asset_income(db=db, financial_asset_income=financial_asset_income, petin = etin)
    else: 
        return crud.update_financial_asset_income(db, financial_asset_income=financial_asset_income, petin = etin)
    

