# from fastapi import FastAPI, Depends, HTTPException, Body, Query
# from sqlalchemy.orm import Session
# import crud, models, schemas
# from db import SessionLocal, engine, get_db


# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()

# @app.post("/investment_record/", response_model=schemas.Investment_Record)
# def create_investment_record(
#     investment_record: schemas.Investment_Record = Body(...),
#     given_premium: schemas.Given_Premium = Body(...),
#     gov_securities: schemas.Gov_Securities = Body(...),
#     eft: schemas.E_FT = Body(...),
#     dps: schemas.D_PS = Body(...),
#     db: Session = Depends(get_db)
# ):
#     # Get the related data
    
#     # Insert the investment record without specifying the `total_investment`
#     crud.create_investment_record(db=db, investment_record=investment_record)
    
   
    
#     given_p = crud.get_given_premium(db, investment_id=given_premium.investment_id)
#     if not given_p:
#         raise HTTPException(status_code=404, detail="GivenPremium not found")
    
#     gov_sec = crud.get_gov_securities(db, investment_id=gov_securities.investment_id)
#     if not gov_sec:
#         raise HTTPException(status_code=404, detail="GovSecurities not found")
    
#     e_ft = crud.get_eft(db, investment_id=eft.investment_id)
#     if not e_ft:
#         raise HTTPException(status_code=404, detail="EFT not found")
    
#     d_ps = crud.get_dps(db, investment_id=dps.investment_id)
#     if not d_ps:
#         raise HTTPException(status_code=404, detail="DPS not found")

    
    

#     inv_record = db.query(models.InvestmentRecord).filter(models.InvestmentRecord.etin == investment_record.etin).first()

#     if inv_record:
#         inv_record.gov_securities_actual = gov_sec.actual
#         inv_record.gov_securities_allowable = gov_sec.allowable
        
#         inv_record.eft_actual = e_ft.actual
#         inv_record.eft_allowable = e_ft.allowable
        
#         inv_record.life_insurance_given_premium_actual = given_p.given_premium
#         inv_record.life_insurance_given_premium_allowable = given_p.allowable
        
#         inv_record.contribution_paid_to_deposit_pension_actual = d_ps.actual
#         inv_record.contribution_paid_to_deposit_pension_allowable = d_ps.allowable
        
#         db.commit()
#         db.refresh(inv_record)
#     else:
#         raise HTTPException(status_code=404, detail="InvestmentRecord not found")
    
#     return investment_record

    
    

# @app.get("/investment_record/{etin}", response_model=schemas.Investment_Record)
# def read_investment_record(etin: str, db: Session = Depends(get_db)):
#     db_item = crud.get_investment_record(db, etin= etin)
#     if db_item is None:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return db_item


# @app.get("/investment_records/", response_model=list[schemas.Investment_Record])
# def read_investment_records(skip: int = Query(...), limit: int = Query(...), db: Session = Depends(get_db)):
#     items = crud.get_investment_records(db, skip=skip, limit=limit)
#     return items





from fastapi import FastAPI, Depends, HTTPException, Body, Query, Path
from sqlalchemy.orm import Session
import crud, models, schemas
from db import get_db

# models.Base.metadata.create_all(bind=models.engine)

app = FastAPI()

@app.post("/investment_record/", response_model=schemas.Investment_Record)
def create_investment_record(
    investment_record: schemas.Investment_Record = Body(...),
    given_premium: schemas.Given_Premium = Body(...),
    gov_securities: schemas.Gov_Securities = Body(...),
    eft: schemas.E_FT = Body(...),
    dps: schemas.D_PS = Body(...),
    etin : str = Body(...),
    db: Session = Depends(get_db)
):
    
    try:
    # Start a transaction
        db.begin()

        # Step 1: Add the investment record
        crud.create_investment_record(db, investment_record, etin)
        
        investment = crud.get_investment_record(db, etin)

        
        crud.create_given_premium(db, given_premium, investment.etin)
        crud.create_gov_securities(db, gov_securities, investment.etin)
        crud.create_eft(db, eft, investment.etin)
        crud.create_dps(db, dps, investment.etin)

        # Step 3: Fetch and update `InvestmentRecord` with calculated data
        inv_record = (
            db.query(models.InvestmentRecord)
            .filter(models.InvestmentRecord.etin == investment.etin)
            .first()
        )

        if not inv_record:
            raise HTTPException(status_code=404, detail="InvestmentRecord not found")

        inv_record.gov_securities_actual = gov_securities.actual
        inv_record.gov_securities_allowable = gov_securities.allowable

        inv_record.eft_actual = eft.actual
        inv_record.eft_allowable = eft.allowable

        inv_record.life_insurance_given_premium_actual = given_premium.given_premium
        inv_record.life_insurance_given_premium_allowable = given_premium.allowable

        inv_record.contribution_paid_to_deposit_pension_actual = dps.actual
        inv_record.contribution_paid_to_deposit_pension_allowable = dps.allowable

        db.commit()  # Commit the transaction
        db.refresh(inv_record)

        return inv_record

    except Exception as e:
        db.rollback()  # Rollback on error
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    
    

@app.get("/investment_record/{etin}", response_model=schemas.Investment_Record)
def read_investment_record(etin: str = Path(...), db: Session = Depends(get_db)):
    db_item = crud.get_investment_record(db, etin=etin)
    if not db_item:
        raise HTTPException(status_code=404, detail=f"Investment record for ETIN {etin} not found")
    return db_item


@app.get("/investment_records/", response_model=list[schemas.Investment_Record])
def read_investment_records(skip: int = Query(...), limit: int = Query(...), db: Session = Depends(get_db)):
    items = crud.get_investment_records(db, skip=skip, limit=limit)
    if not items:
        raise HTTPException(status_code=404, detail="No investment records found")
    return items
