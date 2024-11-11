from sqlalchemy import Column, Integer, String, Enum as senum, Date, JSON, ForeignKey
from sqlalchemy.orm import relationship
from db import Base
from enum import Enum


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

    # id = Column(Integer, primary_key= True, nullable= False, unique= True, index= True)
    etin = Column (String(12), primary_key= True, unique= True, index= True, nullable= False)
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
    
    
    private_salary_income_records = relationship("PrivateSalaryIncomeRecord", back_populates="TaxPayer")
    gov_salary_income_records = relationship("GovSalaryIncomeRecord", back_populates="TaxPayer")
    
    
    
    
    
class PrivateSalaryIncomeRecord(Base):
    __tablename__ = "private_salary_income_records"  # Use the correct table name

    id = Column(Integer, primary_key=True, index=True, unique= True)
    basic_salary = Column(Integer, nullable=False)
    house_rent_allowance = Column(Integer, nullable=False)
    medical_allowance = Column(Integer, nullable=False)
    festival_bonus = Column(Integer, nullable=False)
    rent_free_accommodation = Column(Integer, default=0)
    accommodation_at_concessional_rate = Column(Integer, default=0)
    rent_paid_by_taxpayer = Column(Integer, default=0)
    vehicle_facility_months = Column(Integer, default=0)
    is_higher_cc = Column(String, default='N')  # 'Y' or 'N'
    other_non_cash_benefits = Column(Integer, default=0)  # Store as JSON (dictionary)
    num_autistic_children = Column(Integer, default=0)
    arrear_salary = Column(Integer, default=0)
    education_allowance = Column(Integer, default=0)
    entertainment_allowance = Column(Integer, default=0)
    employer_contribution_RPF = Column(Integer, default=0)
    gratuity = Column(Integer, default=0)
    interest_accrued_RPF = Column(Integer, default=0)
    leave_allowance = Column(Integer, default=0)
    other_bonus = Column(Integer, default=0)
    overtime = Column(Integer, default=0)
    pension = Column(Integer, default=0)
    tada = Column(Integer, default=0)
    income_from_employee_share_scheme = Column(Integer, default=0)
    others = Column(Integer, default=0)
    fee = Column(Integer, default=0)
    commission = Column(Integer, default=0)
    mohargha_allowance = Column(Integer, default=0)
    allowances = Column(Integer, default=0)
    perquisites = Column(Integer, default=0)
    
    etin = Column(String(12), ForeignKey('TaxPayer.etin'), nullable=False)

    # Define a relationship to the Taxpayer table
    TaxPayer = relationship("TaxPayer", back_populates="private_salary_income_records")
    
    
    
    
    
class GovSalaryIncomeRecord(Base):
    __tablename__ = "gov_salary_income_records"  # Use the correct table name

    id = Column(Integer, primary_key=True, index=True, unique= True)
    basic_salary = Column(Integer, nullable=False)
    house_rent_allowance = Column(Integer, nullable=False)
    medical_allowance = Column(Integer, nullable=False)
    festival_allowance = Column(Integer, nullable=False)
    arrear_pay = Column(Integer, default=0)
    special_allowance = Column(Integer, default=0)
    conveyance_allowance = Column(Integer, default=0)
    support_staff_allowance = Column(Integer, default=0)
    leave_allowance = Column(Integer, default=0)
    reward = Column(Integer, default=0)
    overtime = Column(Integer, default=0)
    bangla_noboborsho = Column(Integer, default=0)
    interest_accrued_from_PF = Column(Integer, default=0)
    lump_grant = Column(Integer, default=0)
    gratuity = Column(Integer, default=0)
    others = Column(Integer, default=0)
    
    etin = Column(String(12), ForeignKey('TaxPayer.etin'), nullable=False)

    # Define a relationship to the Taxpayer table
    TaxPayer = relationship("TaxPayer", back_populates="gov_salary_income_records")
    
    