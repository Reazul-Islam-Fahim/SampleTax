from fastapi import FastAPI, HTTPException, Query, Body, Depends
from sqlalchemy.orm import Session
from db import get_db
from fastapi.middleware.cors import CORSMiddleware
import schemas,crud


# origins = [
#     "https://localhost:8000",
#     "https://yourfrontenddomain.com",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins = origins,
#     allow_credentials = True,
#     allow_methods = ['*'],
#     allow_headers = ['*']
# )



app = FastAPI()

@app.post("/calculate_rebate/", response_model=schemas.Rebate_Record)
def create_rebate_record(rebate_record: schemas.Rebate_Record = Body(...), db: Session = Depends(get_db)):
    return crud.create_tax_payer(db=db, rebate_record=rebate_record)


@app.get("/get_rebate/{tax_payer_id}", response_model=schemas.Rebate_Record)
def read_rebate_record(etin: str, db: Session = Depends(get_db)):
    db_item = crud.get_tax_payer(db, etin= etin)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.get("/get_rebates/", response_model=list[schemas.Rebate_Record])
def read_rebate_records(skip: int = Query(...), limit: int = Query(...), db: Session = Depends(get_db)):
    items = crud.get_tax_payers(db, skip=skip, limit=limit)
    return items