from sqlalchemy import Column, Integer, String, VARCHAR, Enum as senum
from db import Base
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"
    
    
class EmploymentType(str, Enum):
    gov = "government"
    private = "private"


class Taxpayer(Base):
    __tablename__ = "TaxPayer"

    id = Column(Integer, primary_key= True, nullable= False, unique= True, index= True)
    etin = Column (String(12), unique= True, index= True, nullable= False)
    name = Column(String(100), index = True, nullable= False)
    gender = Column(senum(Gender), index=True, nullable= False)
    employment_type = Column(senum(EmploymentType), index= True, nullable= False)
    company_name = Column(String(500), index = True, nullable= False)
    
    
    
    