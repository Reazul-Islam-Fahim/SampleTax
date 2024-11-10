from sqlalchemy.orm import Session
import models, schemas

def get_tax_payer(db: Session, tax_payer_id: int):
    return db.query(models.Taxpayer).filter(models.Taxpayer.id == tax_payer_id).first()

def get_tax_payers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Taxpayer).offset(skip).limit(limit).all()

def create_tax_payer(db: Session, tax_payer: schemas.TaxPayerCreate):
    db_item = models.Taxpayer(
        #id = tax_payer.id, 
        name=tax_payer.name, 
        etin=tax_payer.etin, 
        gender = tax_payer.gender, 
        employment_type = tax_payer.employment_type, 
        company_name = tax_payer.company_name
        )
    
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item