from fastapi import FastAPI, HTTPException, Query, Body, Depends
from sqlalchemy.orm import Session
from db import get_db
from fastapi.middleware.cors import CORSMiddleware
import schemas,crud, models, re


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


def calculate_area_tax(zone):
    # Use regular expression to match "Dhaka" in any part of the string
    if re.search(r"\b(DHAKA|CHITTAGONG)\b", zone, re.IGNORECASE):  
        area_tax = 5000
    elif re.search(r"\bCITY\b", zone, re.IGNORECASE):
        area_tax = 4000
    else:
        area_tax = 3000  # Assuming no tax for other zones
    return area_tax


@app.post("/calculate_tax/", response_model=schemas.Tax_Record)
def create_tax_record(
    # tax_record: schemas.Tax_Record = Body(...), 
    etin : str = Query(...), 
    db: Session = Depends(get_db)
    ):
    
    income_summary = crud.get_salary_income_summary(db, etin)
    if not income_summary:
        raise HTTPException(status_code=404, detail="income_summary not found")
    
    rebate_record = crud.get_rebate_record(db, etin)
    if not rebate_record:
        raise HTTPException(status_code=404, detail="rebate_record not found")
    
    taxpayer = crud.get_tax_payer(db, etin)
    if not taxpayer:
        raise HTTPException(status_code=404, detail="Taxpayer not found")
    
    if not taxpayer.zone:
        raise HTTPException(status_code=400, detail="Taxpayer zone not specified")
    
    
    net_tax_liability = income_summary.tax_liability - rebate_record.rebate

    area_tax = calculate_area_tax(taxpayer.zone.upper())
    
    minimum_tax = area_tax
    
    actual_payable_tax = max(net_tax_liability, minimum_tax, area_tax)
    
    tax = crud.create_tax_record(db, petin = etin, net_tax_liability = net_tax_liability, area_tax = area_tax, actual_payable_tax = actual_payable_tax)
    
    return tax



@app.get("/get_tax/{etin}", response_model=schemas.Tax_Record)
def read_tax_record(etin: str, db: Session = Depends(get_db)):
    db_item = crud.get_tax_record(db, etin= etin)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.get("/get_taxes/", response_model=list[schemas.Tax_Record])
def read_tax_records(skip: int = Query(...), limit: int = Query(...), db: Session = Depends(get_db)):
    items = crud.get_tax_records(db, skip=skip, limit=limit)
    return items