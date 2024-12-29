from fastapi import FastAPI, HTTPException, Query, Path, Depends
from sqlalchemy.orm import Session
from db import get_db
from fastapi.middleware.cors import CORSMiddleware
import schemas,crud, models, re
from tax_slab import _calculate_tax_liability


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
    


def calculate_area_tax(source_area):
    # Use regular expression to match "Dhaka" in any part of the string
    if re.search(r"\b(DHAKA|CHITTAGONG)\b", source_area, re.IGNORECASE):  
        area_tax = 5000
    elif re.search(r"\bCITY\b", source_area, re.IGNORECASE):
        area_tax = 4000
    else:
        area_tax = 3000  # Assuming no tax for other zones
    return area_tax


@app.post("/tax/{etin}",)
def create_tax_record(
    etin : str = Path(...), 
    db: Session = Depends(get_db)
    ):
    
    salary_income_summary = crud.get_salary_income_summary(db, etin)
    if not salary_income_summary:
        raise HTTPException(status_code=404, detail="income_summary not found")
    
    rebate_record = crud.get_rebate_record(db, etin)
    if not rebate_record:
        raise HTTPException(status_code=404, detail="rebate_record not found")
    
    taxpayer = crud.get_tax_payer(db, etin)
    if not taxpayer:
        raise HTTPException(status_code=404, detail="Taxpayer not found")
    
    if not taxpayer.source_area:
        raise HTTPException(status_code=400, detail="Taxpayer source area not specified")
    
    financial_asset_income = crud.get_financial_asset_income(db, etin)
    if not financial_asset_income:
        raise HTTPException(status_code=404, detail="financial_asset_income not found")
    
    rent_income_summary = crud.get_rent_summary_income(db, etin)
    

    area_tax = calculate_area_tax(taxpayer.source_area.upper())
    
    total_liability_regular_minimum_income = _calculate_tax_liability(salary_income_summary.taxable_income + financial_asset_income.total_taxable + rent_income_summary.gross_net_income - financial_asset_income.savings_ban_interest_taxable)
    
    tax_liability_except_final_exempted_minimum = _calculate_tax_liability(salary_income_summary.taxable_income + rent_income_summary.gross_net_income)
    
    minimum_tax = total_liability_regular_minimum_income - tax_liability_except_final_exempted_minimum
    
    ait = financial_asset_income.total_tax_deduction_at_source - financial_asset_income.savings_ban_interest_tax_deduction_at_source
    
    minimum_tax = max(minimum_tax, ait)
    
    total_tax = tax_liability_except_final_exempted_minimum + minimum_tax
    
    final_tax = financial_asset_income.savings_ban_interest_tax_deduction_at_source
    
    total_tax_liability = total_tax + final_tax
    
    net_tax_liability = total_tax_liability - rebate_record.rebate
    
    actual_payable_tax = max(net_tax_liability, minimum_tax, area_tax)
    
    tax = crud.create_tax_record(db, petin = etin, net_tax_liability = net_tax_liability, area_tax = area_tax, min_tax = minimum_tax, actual_payable_tax = actual_payable_tax)
    
    return tax



@app.get("/tax/{etin}", response_model=schemas.Tax_Record)
def read_tax_record(etin: str, db: Session = Depends(get_db)):
    db_item = crud.get_tax_record(db, etin= etin)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.get("/tax/", response_model=list[schemas.Tax_Record])
def read_tax_records(skip: int = Query(...), limit: int = Query(...), db: Session = Depends(get_db)):
    items = crud.get_tax_records(db, skip=skip, limit=limit)
    return items