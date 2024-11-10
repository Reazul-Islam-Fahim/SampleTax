from pydantic import BaseModel
from models import *
from datetime import date


class TaxPayers(BaseModel):
    name: str
    nid : int
    etin : int
    circle : str
    zone : str
    assesment_year : str
    residential_status : ResidentialStatus
    gender : Gender
    employment_type : EmploymentType
    company_name : str
    freedom_fighter : FreedomFighter
    disable : Disable
    parent_of_disable : ParentOfDiasable
    age_above_65 : AgeAbove65
    date_of_birth : date
    Spouse_name : str
    spouse_tin : int | None = None
    address : str
    telephone : str | None = None
    mobile : str
    email : str
    employer_name : str
    name_of_organization : str
    bin_no : str
    name_tin_partners : str |None = None 
    

class TaxPayerCreate(TaxPayers):
    pass

class TaxPayer(TaxPayers):
    pass

    class Config:
        orm_mode = True