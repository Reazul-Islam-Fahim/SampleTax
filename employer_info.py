from fastapi import FastAPI, Depends, HTTPException, Body, Query
from sqlalchemy.orm import Session
import crud, models, schemas
from db import SessionLocal, engine, get_db


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/employer_info/{employer_info_id}", response_model=schemas.Employer_info)
def read_employer_info(etin: str, db: Session = Depends(get_db)):
    db_item = crud.get_employer_info(db, etin=etin)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Employer info not found")
    return db_item

@app.get("/employer_infos/", response_model=list[schemas.Employer_info])
def read_employer_infos(skip: int = Query(...), limit: int = Query(...), db: Session = Depends(get_db)):
    items = crud.get_employer_infos(db, skip=skip, limit=limit)
    return items

@app.post("/employer_info/", response_model=schemas.Employer_info)
def create_employer_info_route(employer_info: schemas.Employer_info = Body(...), etin : str = Body(...), db: Session = Depends(get_db)):
    user = crud.get_tax_payer(db, etin)
    print(user)
    return crud.create_employer_info(db=db, employer_info=employer_info, petin= user.etin)