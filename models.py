from sqlalchemy import Column, Integer, String, Enum as senum, ForeignKey
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

class  ParentOfDisable(str, Enum):
    yes = "Yes"
    no = "No"

class  AgeAbove65(str, Enum):
    yes = "Yes"
    no = "No"






class Taxpayer(Base):
    __tablename__ = "taxpayer"


    # id = Column(Integer, primary_key= True, nullable= False, unique= True, index= True)
    etin = Column (String(12), primary_key= True, unique= True, index= True, nullable= False)
    nid = Column (String(12), unique= True, index= True, nullable= False)
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
    parent_of_disable = Column(senum(ParentOfDisable), index= True, nullable= False)
    num_autistic_children = Column(Integer, default=0)
    age_above_65 = Column(senum(AgeAbove65), index= True, nullable= False)
    date_of_birth = Column(String, index= True, nullable= False)
    spouse_name = Column (String(100), index= True, nullable= False)
    spouse_tin = Column(String(12), index= True, nullable= True)
    address = Column (String(500), index= True, nullable= False)
    telephone = Column (String(15), index= True, nullable= True)
    mobile = Column (String(20), unique= True, index= True, nullable= False)
    email = Column (String(120), unique= True, index= True, nullable= False)
    employer_name = Column (String(120), index= True, nullable= False)
    name_of_organization = Column (String(150), index= True, nullable= True)
    bin_no = Column (String(20), unique= True, index= True, nullable= True)
    name_tin_partners = Column (String(1000), index= True, nullable= True)
    
    
    employeer_info = relationship("EmployeerInfo", back_populates="taxpayer")
    salary_income_records = relationship("SalaryIncomeRecord", back_populates="taxpayer")
    allowance_details = relationship("AllowanceDetails", back_populates="taxpayer")
    perquisite_details = relationship("PerquisiteDetails", back_populates="taxpayer")
    vehicle_facility_details = relationship("VehicleFacilityDetails", back_populates="taxpayer")
    salary_income_summary = relationship("SalaryIncomeSummary", back_populates="taxpayer")
    investment_record = relationship("InvestmentRecord", back_populates="taxpayer")
    rebate_record = relationship("RebateRecord", back_populates="taxpayer")
    
    
    
    
class EmployeerInfo(Base):
    __tablename__ = "employeer_info"
    
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String(100), nullable= False)
    start_date = Column(String(10), nullable= False)
    end_date = Column(String(10), nullable= False)
    
    etin = Column(String(12), ForeignKey('taxpayer.etin'), nullable=False)
    
    salary_income_records = relationship("SalaryIncomeRecord", back_populates="employeer_info")
    
    
class SalaryIncomeRecord(Base):
    __tablename__ = "salary_income_records"  # Combined table for both private and government records

    id = Column(Integer, primary_key=True, index=True, unique=True)
    
    # Common fields
    basic_salary = Column(Integer, default=0)
    basic_salary_remarks = Column(String, nullable=True)

    # Private salary fields with 'private_' prefix
    private_allowances = Column(Integer, default=0)
    private_allowances_remarks = Column(String, nullable=True)
    private_arrear_salary = Column(Integer, default=0)
    private_arrear_salary_remarks = Column(String, nullable=True)
    private_gratuity = Column(Integer, default=0)
    private_gratuity_remarks = Column(String, nullable=True)
    private_perquisites = Column(Integer, default=0)
    private_perquisites_remarks = Column(String, nullable=True)
    private_receipts_or_additional_receipts_in_lieu_of_salary_or_wages = Column(Integer, default=0)
    private_receipts_or_additional_receipts_in_lieu_of_salary_or_wages_remarks = Column(String, nullable=True)
    private_income_from_employee_share_scheme = Column(Integer, default=0)
    private_income_from_employee_share_scheme_remarks = Column(String, nullable=True)
    private_housing_facility = Column(Integer, default=0)
    private_housing_facility_remarks = Column(String, nullable=True)
    private_vehicle_facility = Column(Integer, default=0)
    private_vehicle_facility_remarks = Column(String, nullable=True)
    private_any_other_benefit_provided_by_the_employer = Column(Integer, default=0)
    private_any_other_benefit_provided_by_the_employer_remarks = Column(String, nullable=True)
    private_contribution_paid_by_employer_to_recognized_provident_fund = Column(Integer, default=0)
    private_contribution_paid_by_employer_to_recognized_provident_fund_remarks = Column(String, nullable=True)
    private_others = Column(Integer, default=0)
    private_others_remarks = Column(String, nullable=True)

    # Government salary fields with 'gov_' prefix
    gov_arrear_pay = Column(Integer, default=0)
    gov_arrear_pay_remarks = Column(String, nullable=True)
    gov_festival_allowance = Column(Integer, default=0)
    gov_festival_allowance_remarks = Column(String, nullable=True)
    gov_special_allowance = Column(Integer, default=0)
    gov_special_allowance_remarks = Column(String, nullable=True)
    gov_support_staff_allowance = Column(Integer, default=0)
    gov_support_staff_allowance_remarks = Column(String, nullable=True)
    gov_leave_allowance = Column(Integer, default=0)
    gov_leave_allowance_remarks = Column(String, nullable=True)
    gov_reward = Column(Integer, default=0)
    gov_reward_remarks = Column(String, nullable=True)
    gov_overtime = Column(Integer, default=0)
    gov_overtime_remarks = Column(String, nullable=True)
    gov_bangla_noboborsho = Column(Integer, default=0)
    gov_bangla_noboborsho_remarks = Column(String, nullable=True)
    gov_interest_accrued_from_PF = Column(Integer, default=0)
    gov_interest_accrued_from_PF_remarks = Column(String, nullable=True)
    gov_lump_grant = Column(Integer, default=0)
    gov_lump_grant_remarks = Column(String, nullable=True)
    gov_gratuity = Column(Integer, default=0)
    gov_gratuity_remarks = Column(String, nullable=True)
    gov_others = Column(Integer, default=0)
    gov_others_remarks = Column(String, nullable=True)                        # Government (renamed to avoid conflict)
    
    etin = Column(String(12), ForeignKey('taxpayer.etin'), nullable=False)

    # Define a relationship to the Taxpayer table
    taxpayer = relationship("Taxpayer", back_populates="salary_income_records")    
    
    employeer_info = relationship("EmployeerInfo", back_populates="salary_income_records")
    allowance_details = relationship("AllowanceDetails", back_populates="salary_income_records")
    perquisite_details = relationship("PerquisiteDetails", back_populates="salary_income_records")
    vehicle_facility_details = relationship("VehicleFacilityDetails", back_populates="salary_income_records")
    

    
class AllowanceDetails(Base):
    __tablename__ = "allowance_details"
    
    
    id = Column(Integer, primary_key=True, index=True, unique= True)
    any_allowance = Column(Integer, default=0)
    any_allowance_remarks = Column(String, nullable=True)
    leave_allowance = Column(Integer, default=0)
    leave_allowance_remarks = Column(String, nullable=True)
    lump_grant = Column(Integer, default=0)
    lump_grant_remarks = Column(String, nullable=True)
    bonus = Column(Integer, default=0)
    bonus_remarks = Column(String, nullable=True)
    fee = Column(Integer, default=0)
    fee_remarks = Column(String, nullable=True)
    commission = Column(Integer, default=0)
    commission_remarks = Column(String, nullable=True)
    overtime = Column(Integer, default=0)
    overtime_remarks = Column(String, nullable=True)
    other = Column(Integer, default=0)
    other_details = Column(String, nullable=True)
    
    etin = Column(String(12), ForeignKey('taxpayer.etin'), nullable=False)
    
    taxpayer = relationship("Taxpayer", back_populates="allowance_details")
    salary_income_records = relationship("SalaryIncomeRecord", back_populates="allowance_details")
    
    
    
    
class PerquisiteDetails(Base):
    __tablename__ = 'perquisite_details'
    
    id = Column(Integer, primary_key=True, unique=True, index=True)
    mohargha_allowance = Column(Integer, default=0)
    mohargha_allowance_remarks = Column(String, nullable=True)
    insurance_premium_borne_by_the_employer = Column(Integer, default=0)
    insurance_premium_borne_by_the_employer_remarks = Column(String, nullable=True)
    housing_allowance = Column(Integer, default=0)
    housing_allowance_remarks = Column(String, nullable=True)
    house_rent_allowance = Column(Integer, default=0)
    house_rent_allowance_remarks = Column(String, nullable=True)
    entertainment_allowance = Column(Integer, default=0)
    entertainment_allowance_remarks = Column(String, nullable=True)
    passage_leave = Column(Integer, default=0)
    passage_leave_remarks = Column(String, nullable=True)
    medical_allowance = Column(Integer, default=0)
    medical_allowance_remarks = Column(String, nullable=True)
    any_other_obligations_of_the_employee = Column(Integer, default=0)
    any_other_obligations_of_the_employee_remarks = Column(String, nullable=True)
    other = Column(Integer, default=0)
    other_remarks = Column(String, nullable=True)
    total = Column(Integer, default=0)
    
    etin = Column(String(12), ForeignKey('taxpayer.etin'), nullable=False)
    
    taxpayer = relationship("Taxpayer", back_populates="perquisite_details")
    salary_income_records = relationship("SalaryIncomeRecord", back_populates="perquisite_details")
    
    
    
class VehicleFacilityDetails(Base):
    __tablename__ = "vehicle_facility_details"  # Table name in the database

    
    id = Column(Integer, primary_key=True, index=True, unique=True)
    upto_2500CC = Column(String, nullable=False)  # Assuming this is a string (Y/N or description)
    cost_for_upto_2500 = Column(Integer, default=10000)  # Default value as provided
    greater_than_2500cc = Column(String, nullable=False)  # Assuming this is a string (Y/N or description)
    cost_for_more_than_2500 = Column(Integer, default=25000)  # Default value as provided
    no_of_months = Column(Integer, default=0)  # Default value as 0
    total = Column(Integer, default=0)  # Default value as 0
    
    etin = Column(String(12), ForeignKey('taxpayer.etin'), nullable=False)
    
    taxpayer = relationship("Taxpayer", back_populates="vehicle_facility_details")
    salary_income_records = relationship("SalaryIncomeRecord", back_populates="vehicle_facility_details")
    
    
    

class SalaryIncomeSummary(Base):
    __tablename__ = "salary_income_summary"


    id = Column(Integer, primary_key=True, index=True, unique= True)
    total_income = Column(Integer, index= True, default= 0)
    exempted_income = Column(Integer, index= True, default= 0)
    taxable_income = Column(Integer, index= True, default= 0)
    tax_liability = Column(Integer, index= True, default= 0)
    
    etin = Column(String(12), ForeignKey('taxpayer.etin'), nullable=False)
    
    taxpayer = relationship("Taxpayer", back_populates="salary_income_summary")
    
    
    
    
class InvestmentRecord(Base):
    __tablename__ = "investment_record"
    
    
    id = Column(Integer, primary_key=True, index=True, unique= True)
    gov_securities = Column(Integer, index= True, default= 0)
    eft = Column(Integer, index= True, default= 0)
    life_insurance_policy_value = Column(Integer, index= True, default= 0)
    life_insurance_given_premium = Column(Integer, index= True, default= 0)
    other = Column(Integer, index= True, default= 0)
    
    etin = Column(String(12), ForeignKey('taxpayer.etin'), nullable=False)
    
    taxpayer = relationship("Taxpayer", back_populates="investment_record")
    
    
    
    
    
class RebateRecord(Base):
    __tablename__ = "rebate_record"
    
    
    id = Column(Integer, primary_key=True, index=True, unique= True)
    actual_investment = Column(Integer, index= True, default= 0)
    allowable_investment = Column(Integer, index= True, default= 0)
    rebate = Column(Integer, index= True, default= 0)
    
    etin = Column(String(12), ForeignKey('taxpayer.etin'), nullable=False)
    
    taxpayer = relationship("Taxpayer", back_populates="rebate_record")
    
    
    
