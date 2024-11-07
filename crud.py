from sqlalchemy.orm import Session
from . import models, schemas

def get_tax_payer(db: Session, tax_payer_id: int):
    return db.query(models.Taxpayer).filter(models.Taxpayer.id == tax_payer_id).first()

def get_tax_payers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Taxpayer).offset(skip).limit(limit).all()

def create_tax_payer(db: Session, tax_payer: schemas.TaxPayerCreate):
    db_item = models.Taxpayer(name=tax_payer.name, description=tax_payer.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item