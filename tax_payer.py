from fastapi import FastAPI, Depends, HTTPException, Body, Query
from sqlalchemy.orm import Session
import crud, models, schemas
from db import SessionLocal, engine, get_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://192.168.2.33:5173",
    "http://192.168.2.48",
    # "https://yourfrontenddomain.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)


@app.post("/tax_payer/")
def create_tax_payer(taxpayer: schemas.TaxPayerCreate = Body(...), db: Session = Depends(get_db)): 
    return crud.create_tax_payer(db=db, tax_payer=taxpayer, user_id=taxpayer.user_id)

@app.put("/tax_payer/{etin}")
async def update_tax_payer_endpoint(
    updated_tax_payer: schemas.TaxPayerCreate,
    db: Session = Depends(get_db),
):
    updated_record = crud.update_tax_payer(db, updated_tax_payer.etin, updated_tax_payer)
    if updated_record is None:
        raise HTTPException(status_code=404, detail="Taxpayer record not found")
    return updated_record


@app.get("/tax_payer/{etin}")
def read_tax_payer(etin: str, db: Session = Depends(get_db)):
    db_item = crud.get_tax_payer(db, etin= etin)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.get("/tax_payer/")
def read_tax_payers(skip : int = Query(...), limit : int = Query(...), db: Session = Depends(get_db)):
    items = crud.get_tax_payers(db, skip=skip, limit=limit)
    return items


@app.post("/tax_payer_post_update/")
def create_tax_payer(taxpayer: schemas.TaxPayerCreate = Body(...), db: Session = Depends(get_db)): 
    db_item = crud.get_tax_payer(db, etin= taxpayer.etin)
    if db_item is None:
        item = crud.create_tax_payer(db=db, tax_payer=taxpayer, user_id=taxpayer.user_id)
    else:
        item = crud.update_tax_payer(db, taxpayer.etin, taxpayer)
    
    print(item.gender)
        
    return item