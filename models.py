from sqlalchemy import Column, Integer, String, Enum as senum, Date
from db import Base
from enum import Enum
from datetime import date


class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"
    
    
class EmploymentType(str, Enum):
    gov = "government"
    private = "private"


class ResidentialStatus(str, Enum):
    resident = "Resident"
    non_resident = "Non-resident"
    

class TaxPayerStatus(str, Enum):
    individual = "Individual"
    firm = "Firm"
    hindu = "Hindu Undivided Family"
    other = "Others"
    
    
class FreedomFighter(str, Enum):
    yes = "Yes"
    no = "No"

class Disable(str, Enum):
    yes = "Yes"
    no = "No"

class  ParentOfDiasable(str, Enum):
    yes = "Yes"
    no = "No"

class  AgeAbove65(str, Enum):
    yes = "Yes"
    no = "No"






class Taxpayer(Base):
    __tablename__ = "TaxPayer"

    id = Column(Integer, primary_key= True, nullable= False, unique= True, index= True)
    etin = Column (String(12), unique= True, index= True, nullable= False)
    nid = Column (Integer, unique= True, index= True, nullable= False)
    name = Column(String(100), index = True, nullable= False)
    gender = Column(senum(Gender), index=True, nullable= False)
    circle = Column (String(50), index= True, nullable= False)
    zone = Column (String(50), index= True, nullable= False)
    employment_type = Column(senum(EmploymentType), index= True, nullable= False)
    company_name = Column(String(500), index = True, nullable= False)
    assesment_year = Column (String(20), index= True, nullable= False)
    residential_status = Column(senum(ResidentialStatus), index= True, nullable= False)
    freedom_fighter = Column(senum(FreedomFighter), index= True, nullable= False)
    disable = Column(senum(Disable), index= True, nullable= False)
    parent_of_disable = Column(senum(ParentOfDiasable), index= True, nullable= False)
    age_above_65 = Column(senum(AgeAbove65), index= True, nullable= False)
    date_of_birth = Column(Date, index= True, nullable= False)
    Spouse_name = Column (String(100), index= True, nullable= False)
    spouse_tin = Column(Integer, unique= True, index= True)
    address = Column (String(500), index= True, nullable= False)
    telephone = Column (String(15), unique= True, index= True)
    mobile = Column (String(20), unique= True, index= True, nullable= False)
    email = Column (String(120), unique= True, index= True, nullable= False)
    employer_name = Column (String(120), index= True, nullable= False)
    name_of_organization = Column (String(150), index= True, nullable= False)
    bin_no = Column (String(20), unique= True, index= True, nullable= False)
    name_tin_partners = Column (String(1000), index= True)
    
    
    