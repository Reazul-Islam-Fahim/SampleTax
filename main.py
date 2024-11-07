from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from . import crud, models, schemas
from db import SessionLocal, engine, get_db


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/tax_payer/", response_model=schemas.TaxPayer)
def create_tax_payer(taxpayer: schemas.TaxPayerCreate = Query(...), db: Session = Depends(get_db)):
    return crud.create_tax_payer(db=db, taxpayer=taxpayer)

@app.get("/tax_payer/{tax_payer_id}", response_model=schemas.TaxPayer)
def read_tax_payer(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_tax_payer(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.get("/tax_payers/", response_model=list[schemas.TaxPayer])
def read_tax_payers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = crud.get_tax_payers(db, skip=skip, limit=limit)
    return items