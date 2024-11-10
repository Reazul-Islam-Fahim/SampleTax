from pydantic import BaseModel
from models import *
from datetime import date


class TaxPayers(BaseModel):
    id : int
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
    dob : date
    Spouse_name : str
    spouse_tin : int
    address : str
    telephone : str
    mobile : str
    email : str
    employer_name : str
    name_of_organization : str
    bin_no : str
    name_tin_partners : str
    

class TaxPayerCreate(TaxPayers):
    pass

class TaxPayer(TaxPayers):
    pass

    class Config:
        orm_mode = True