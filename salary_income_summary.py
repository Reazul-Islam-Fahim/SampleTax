from fastapi import FastAPI, Depends, HTTPException, Body, Query
from sqlalchemy.orm import Session
import crud, models, schemas
from db import SessionLocal, engine, get_db
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

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



@app.post("/salary_summary/", response_model=schemas.SalaryIncome_Summary)
def create_salary_summary(etin: str = Body(...), db: Session = Depends(get_db)): 
    return crud.create_salary_income_summary(db=db, etin=etin)

@app.put("/salary-income-summary/{etin}", response_model=schemas.SalaryIncome_Summary)
async def update_salary_income_summary_endpoint(
    etin: str,
    updated_summary: schemas.SalaryIncome_Summary,
    db: Session = Depends(get_db),
):
    updated_record = crud.update_salary_income_summary(db, etin, updated_summary)

    if updated_record is None:
        raise HTTPException(status_code=404, detail="SalaryIncomeSummary record not found")

    return updated_record


@app.get("/salary_summary/{tax_payer_id}", response_model=schemas.SalaryIncome_Summary)
def read_salary_summary(etin: str, db: Session = Depends(get_db)):
    db_item = crud.get_salary_income_summary(db, etin= etin)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    total = db_item.total_income
    print(total)
    return total

@app.get("/salary_summarys/", response_model=list[schemas.SalaryIncome_Summary])
def read_salary_summarys(skip: int = Query(...), limit: int = Query(...), db: Session = Depends(get_db)):
    items = crud.get_salary_income_summarys(db, skip=skip, limit=limit)
    return items