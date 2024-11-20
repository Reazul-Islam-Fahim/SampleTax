from fastapi import FastAPI, Depends, HTTPException, Body, Query
from sqlalchemy.orm import Session
import crud, models, schemas
from db import SessionLocal, engine, get_db


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



models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/tax_payer/", response_model=schemas.TaxPayers)
def create_tax_payer(taxpayer: schemas.TaxPayerCreate = Body(...), db: Session = Depends(get_db)): #Body(...) can be use instead of Query(...) for json format
    return crud.create_tax_payer(db=db, tax_payer=taxpayer)

@app.get("/tax_payer/{tax_payer_id}", response_model=schemas.TaxPayers)
def read_tax_payer(etin: str, db: Session = Depends(get_db)):
    db_item = crud.get_tax_payer(db, etin= etin)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.get("/tax_payers/", response_model=list[schemas.TaxPayers])
def read_tax_payers(skip: int = Query(...), limit: int = Query(...), db: Session = Depends(get_db)):
    items = crud.get_tax_payers(db, skip=skip, limit=limit)
    return items