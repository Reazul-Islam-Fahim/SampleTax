from pydantic import BaseModel
from enum import Enum
from models import Gender, EmploymentType


class TaxPayers(BaseModel):
    id : int
    name: str
    etin : int
    gender : Gender
    employment_type : EmploymentType
    company_name : str

class TaxPayerCreate(TaxPayers):
    pass

class TaxPayer(TaxPayers):
    pass

    class Config:
        orm_mode = True