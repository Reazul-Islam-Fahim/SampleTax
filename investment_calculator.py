from fastapi import FastAPI, Depends, HTTPException, Body, Query
from sqlalchemy.orm import Session
import crud, models, schemas
from db import SessionLocal, engine, get_db


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/investment_record/", response_model=schemas.Investment_Record)
def create_investment_record(investment_record: schemas.Investment_Record = Body(...), db: Session = Depends(get_db)): #Body(...) can be use instead of Query(...) for json format
    return crud.create_investment_record(db=db, investment_record=investment_record)

@app.get("/investment_record/{investment_record_id}", response_model=schemas.Investment_Record)
def read_investment_record(etin: str, db: Session = Depends(get_db)):
    db_item = crud.get_investment_record(db, etin= etin)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.get("/investment_records/", response_model=list[schemas.Investment_Record])
def read_investment_records(skip: int = Query(...), limit: int = Query(...), db: Session = Depends(get_db)):
    items = crud.get_investment_records(db, skip=skip, limit=limit)
    return items

# @app.get("/calculate_allowable_investment/{investment_record_id}", response_model=schemas.Investment_Record)
# def calc_allowable_investment(etin : str, db : Session = Depends(get_db)):
#     pass