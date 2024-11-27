from fastapi import FastAPI, HTTPException, Query, Body, Depends
from sqlalchemy.orm import Session
from db import get_db
from fastapi.middleware.cors import CORSMiddleware
import schemas,crud, models


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


@app.post("/calculate_rebate/", response_model=schemas.Rebate_Record)
def create_rebate_record(rebate_record: schemas.Rebate_Record = Body(...), etin : str = Body(...), db: Session = Depends(get_db)):
    
    try:
        investment_amount_record = (
                    db.query(models.InvestmentRecord)
                    .filter(models.InvestmentRecord.etin == etin)
                    .first()
                )
        if not investment_amount_record:
            raise HTTPException(
                status_code=404,
                detail=f"No InvestmentRecord found for ETIN {etin}"
            )
        
        salary_amount_record = (
                    db.query(models.SalaryIncomeSummary)
                    .filter(models.SalaryIncomeSummary.etin == etin)
                    .first()
                )
        if not salary_amount_record:
            raise HTTPException(
                status_code=404,
                detail=f"No SalaryIncomeSummary found for ETIN {etin}"
            )
        
        taxable_income = salary_amount_record.taxable_income
        allowable_investment = investment_amount_record.allowable_investment
        
        rebate = min(taxable_income*0.03, allowable_investment*0.1, 1000000)
        
        rebate_record = crud.create_rebate_record(
            db=db, 
            rebate_record=rebate, 
            petin=etin,
            taxable_income=taxable_income, 
            allowable_investment=allowable_investment
            )
        
        return rebate_record

        
    except Exception as e:
            db.rollback()  # Rollback on error
            raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")





@app.get("/get_rebate/{tax_payer_id}", response_model=schemas.Rebate_Record)
def read_rebate_record(etin: str, db: Session = Depends(get_db)):
    db_item = crud.get_tax_record(db, etin= etin)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.get("/get_rebates/", response_model=list[schemas.Rebate_Record])
def read_rebate_records(skip: int = Query(...), limit: int = Query(...), db: Session = Depends(get_db)):
    items = crud.get_tax_records(db, skip=skip, limit=limit)
    return items