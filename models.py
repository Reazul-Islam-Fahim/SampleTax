from sqlalchemy import Column, Integer, String, VARCHAR, Enum
from db import Base
from enum import Enum


class Gender(Enum):
    male = "male"
    female = "female"
    other = "other"


class Taxpayer(Base):
    __tablename__ = "TaxPayer"

    id = Column(Integer, primary_key= True, nullable= False, unique= True, index= True)
    etin = Column (String(12), unique= True, index= True, nullable= False)
    name = Column(String(100), index = True, nullable= False)
    gender = Column(Enum(Gender), index=True, nullable= False)
    employment_type = Column(Enum(Gender), index= True, nullable= False)
    company_name = Column(String(500), index = True, nullable= False)
    
    
    
    