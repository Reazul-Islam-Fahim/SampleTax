from pydantic import BaseModel
from enum import Enum

class TaxPayers(BaseModel):
    name: str
    description: str

class TaxPayerCreate(TaxPayers):
    pass

class TaxPayer(TaxPayers):
    id: int

    class Config:
        orm_mode = True