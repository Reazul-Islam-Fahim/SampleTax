from fastapi import FastAPI, Depends, HTTPException, Body, Query, Path
from sqlalchemy.orm import Session
import crud, models, schemas
from db import get_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


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
        
        # Step 1: Add the investment record
        crud.create_investment_record(db, investment_record, etin)
        
        investment = crud.get_investment_record(db, etin)
        
        inv_record = (
                db.query(models.InvestmentRecord)
                .filter(models.InvestmentRecord.etin == investment.etin)
                .first()
            )

        
        inv_record.gov_securities_actual = gov_securities.actual
        inv_record.gov_securities_allowable = gov_securities.allowable

        inv_record.eft_actual = eft.actual
        inv_record.eft_allowable = eft.allowable

        inv_record.life_insurance_given_premium_actual = given_premium.given_premium
        inv_record.life_insurance_given_premium_allowable = given_premium.allowable

        inv_record.contribution_paid_to_deposit_pension_actual = dps.actual
        inv_record.contribution_paid_to_deposit_pension_allowable = dps.allowable

        # inv_record.total_investment = inv_record.total_investment
        # inv_record.allowable_investment = inv_record.allowable_investment
        
        inv_record.total_investment = (
            inv_record.gov_securities_actual +
            inv_record.eft_actual +
            inv_record.life_insurance_given_premium_actual +
            inv_record.premium_or_contractual_deferred_annuity_actual +
            inv_record.contribution_paid_to_deposit_pension_actual +
            inv_record.investment_in_any_securities_actual +
            inv_record.provisions_of_pf_act_1925_actual +
            inv_record.contributions_to_approved_provident_fund_actual +
            inv_record.contributions_to_superannuation_funds_actual +
            inv_record.contribution_to_welfare_fund_actual +
            inv_record.contribution_to_zakat_fund_actual +
            inv_record.donation_to_liberation_war_memory_actual +
            inv_record.donations_to_father_of_nation_memory_actual +
            inv_record.donation_to_disabled_organizations_actual +
            inv_record.donations_to_liberation_war_museum_actual +
            inv_record.donation_to_ahsania_cancer_hospital_actual +
            inv_record.donations_to_icddrb_actual +
            inv_record.donation_to_crp_savar_actual +
            inv_record.donations_to_charitable_educational_institutions_actual +
            inv_record.donation_to_asiatic_society_actual +
            inv_record.donation_to_dhaka_ahsania_mission_actual +
            inv_record.contribution_to_super_annuity_fund_actual +
            inv_record.other_actual
        )

    # Calculate allowable_investment
        inv_record.allowable_investment = (
            inv_record.gov_securities_allowable +
            inv_record.eft_allowable +
            inv_record.life_insurance_given_premium_allowable +
            inv_record.premium_or_contractual_deferred_annuity_allowable +
            inv_record.contribution_paid_to_deposit_pension_allowable +
            inv_record.investment_in_any_securities_allowable +
            inv_record.provisions_of_pf_act_1925_allowable +
            inv_record.contributions_to_approved_provident_fund_allowable +
            inv_record.contributions_to_superannuation_funds_allowable +
            inv_record.contribution_to_welfare_fund_allowable +
            inv_record.contribution_to_zakat_fund_allowable +
            inv_record.donation_to_liberation_war_memory_allowable +
            inv_record.donations_to_father_of_nation_memory_allowable +
            inv_record.donation_to_disabled_organizations_allowable +
            inv_record.donations_to_liberation_war_museum_allowable +
            inv_record.donation_to_ahsania_cancer_hospital_allowable +
            inv_record.donations_to_icddrb_allowable +
            inv_record.donation_to_crp_savar_allowable +
            inv_record.donations_to_charitable_educational_institutions_allowable +
            inv_record.donation_to_asiatic_society_allowable +
            inv_record.donation_to_dhaka_ahsania_mission_allowable +
            inv_record.contribution_to_super_annuity_fund_allowable +
            inv_record.other_allowable
        )

        
        
        print(inv_record.total_investment)
        
        print(inv_record.allowable_investment)
        

        
        crud.create_given_premium(db, given_premium, investment.etin)
        crud.create_gov_securities(db, gov_securities, investment.etin)
        crud.create_eft(db, eft, investment.etin)
        crud.create_dps(db, dps, investment.etin)

        # Step 3: Fetch and update `InvestmentRecord` with calculated data
        
        if not inv_record:
            raise HTTPException(status_code=404, detail="InvestmentRecord not found")

        
        print(inv_record)

        return inv_record

    except Exception as e:
        db.rollback()  # Rollback on error
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    
    
    
@app.put("/investment_record/{etin}", response_model=schemas.Investment_Record)
async def update_investment_record_endpoint(
    etin: str,
    updated_record: schemas.Investment_Record,
    db: Session = Depends(get_db),
):
  
    updated_investment_record = crud.update_investment_record(db, etin, updated_record)

    if updated_investment_record is None:
        raise HTTPException(status_code=404, detail="Investment record not found")

    return updated_investment_record

    
    

@app.get("/investment_record/{etin}", response_model=schemas.Investment_Record)
def read_investment_record(etin: str = Path(...), db: Session = Depends(get_db)):
    db_item = crud.get_investment_record(db, etin=etin)
    if not db_item:
        raise HTTPException(status_code=404, detail=f"Investment record for ETIN {etin} not found")
    return db_item


@app.get("/investment_record/", response_model=list[schemas.Investment_Record])
def read_investment_records(skip: int = Query(...), limit: int = Query(...), db: Session = Depends(get_db)):
    items = crud.get_investment_records(db, skip=skip, limit=limit)
    if not items:
        raise HTTPException(status_code=404, detail="No investment records found")
    return items
