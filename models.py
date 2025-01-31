from sqlalchemy import Column, Integer, String, Enum as senum, ForeignKey, Computed
from sqlalchemy.orm import relationship
from db import Base
from enum import Enum


class SourceArea(str, Enum):
    dhaka_chittagong = "dhaka_chittagong"
    city = "city"
    other = "other"



class Gender(str, Enum):
    male = "male"
    female = "female"
    other = "other"
    
    
class EmploymentType(str, Enum):
    gov = "government"
    private = "private"


class ResidentialStatus(str, Enum):
    resident = "resident"
    non_resident = "non-resident"
    

class TaxPayerStatus(str, Enum):
    individual = "individual"
    firm = "firm"
    hindu = "hindu undivided family"
    other = "others"
    
    
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
    
class MaritalStatus(str,Enum):
    married = "married"
    unmarried = "unmarried"
    
    
class AreaType(str, Enum):
    residential = "residential"
    business = "business"
    other = "Other"
    
    
class LiveOwnself(str, Enum):
    yes = "Yes"
    no = "No"
    
    
class Months(str, Enum):
    yes = "Yes"
    no = "No"



class UserAuth(Base):
    __tablename__ = "user_auth"
    
    
    id = Column(Integer, primary_key= True, nullable= False, unique= True, index= True)
    username = Column(String(50), unique= True, nullable= False)
    email = Column(String(50), unique= True, nullable= False)
    password = Column(String(50), nullable= False)


    taxpayer = relationship("Taxpayer", back_populates="user_auth")



class Taxpayer(Base):
    __tablename__ = "taxpayer"


    # id = Column(Integer, primary_key= True, nullable= False, unique= True, index= True)
    etin = Column (String(12), primary_key= True, unique= True, index= True, nullable= False)
    nid = Column (String(12), unique= True, index= True, nullable= False)
    name = Column(String(100), index = True, nullable= False)
    gender = Column(senum(Gender), index=True, nullable= False)
    source_area = Column(senum(SourceArea, name="source_area"), index=True, nullable= False)
    circle = Column (String(50), index= True, nullable= False)
    zone = Column (String(50), index= True, nullable= False)
    employment_type = Column(senum(EmploymentType), index= True, nullable= False)
    company_name = Column(String(500), index = True, nullable= False)
    assesment_year = Column (String(20), index= True, nullable= False)
    residential_status = Column(senum(ResidentialStatus), index= True, nullable= False)
    tax_payer_status = Column(senum(TaxPayerStatus), index= True, nullable= False)
    freedom_fighter = Column(senum(FreedomFighter), index= True, nullable= False)
    disable = Column(senum(Disable), index= True, nullable= False)
    parent_of_disable = Column(senum(ParentOfDisable), index= True, nullable= False)
    num_autistic_children = Column(Integer, default=0)
    age_above_65 = Column(senum(AgeAbove65), index= True, nullable= False)
    date_of_birth = Column(String, index= True, nullable= False)
    father_name = Column (String(100), index= True, nullable= False)
    marital_status = Column (senum(MaritalStatus), index= True, nullable= False)
    spouse_name = Column (String(100), index= True, nullable= False)
    spouse_tin = Column(String(12), index= True, nullable= True)
    permanent_address = Column (String(500), index= True, nullable= False)
    present_address = Column (String(500), index= True, nullable= False)
    telephone = Column (String(15), index= True, nullable= True)
    mobile = Column (String(20), unique= True, index= True, nullable= False)
    email = Column (String(120), unique= True, index= True, nullable= False)
    employer_name = Column (String(120), index= True, nullable= False)
    name_of_organization = Column (String(150), index= True, nullable= True)
    bin_no = Column (String(20), unique= True, index= True, nullable= True)
    name_tin_partners = Column (String(1000), index= True, nullable= True)
    
    
    user_id = Column(Integer, ForeignKey('user_auth.id'), nullable=False)
    user_auth = relationship("UserAuth", back_populates="taxpayer")

    
    
    
    employer_info = relationship("EmployerInfo", back_populates="taxpayer")
    tax_slab = relationship("TaxSlab", back_populates="taxpayer")
    salary_income_records = relationship("SalaryIncomeRecord", back_populates="taxpayer")
    allowance_details = relationship("AllowanceDetails", back_populates="taxpayer")
    perquisite_details = relationship("PerquisiteDetails", back_populates="taxpayer")
    vehicle_facility_details = relationship("VehicleFacilityDetails", back_populates="taxpayer")
    salary_income_summary = relationship("SalaryIncomeSummary", back_populates="taxpayer")
    investment_record = relationship("InvestmentRecord", back_populates="taxpayer")
    given_premium = relationship("GivenPremium", back_populates="taxpayer")
    gov_securities = relationship("GovSecurities", back_populates="taxpayer")
    eft = relationship("EFT", back_populates="taxpayer")
    dps = relationship("DPS", back_populates="taxpayer")
    financial_asset_income = relationship("FinancialAssetIncome", back_populates="taxpayer")
    rent_income_details = relationship("RentIncomeDetails", back_populates="taxpayer")
    rent_income_master = relationship("RentIncomeMaster", back_populates="taxpayer")
    rent_income_summary = relationship("RentIncomeSummary", back_populates="taxpayer")
    rebate_record = relationship("RebateRecord", back_populates="taxpayer")
    tax = relationship("TaxRecord", back_populates="taxpayer")
    
    
    
    
class EmployerInfo(Base):
    __tablename__ = "employer_info"
    
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String(100), nullable= False)
    start_date = Column(String(10), nullable= False)
    end_date = Column(String(10), nullable= False)
    
    etin = Column(String(12), ForeignKey('taxpayer.etin'), nullable=False)
    
    taxpayer = relationship("Taxpayer", back_populates="employer_info")
    salary_income_records = relationship("SalaryIncomeRecord", back_populates="employer_info")
    allowance_details = relationship("AllowanceDetails", back_populates="employer_info")
    perquisite_details = relationship("PerquisiteDetails", back_populates="employer_info")
    vehicle_facility_details = relationship("VehicleFacilityDetails", back_populates="employer_info")
    

class TaxSlab(Base):
    __tablename__ = "tax_slab"
    
    id = Column(Integer, primary_key=True, index=True, unique=True)
    first = Column(Integer, default=0)
    second = Column(Integer, default=0)
    third = Column(Integer, default=0)
    fourth = Column(Integer, default=0)
    fifth = Column(Integer, default=0)
    sixth = Column(Integer, default=0)
    seventh = Column(Integer, default=0)
    
    etin = Column(String(12), ForeignKey('taxpayer.etin'), nullable=False)
    
    taxpayer = relationship("Taxpayer", back_populates="tax_slab")
    

    
    
class SalaryIncomeRecord(Base):
    __tablename__ = "salary_income_records"  # Combined table for both private and government records

    id = Column(Integer, primary_key=True, index=True, unique=True)
    
    # Common fields
    basic_salary = Column(Integer, default=0)
    basic_salary_exempted = Column(Integer, default=0)
    basic_salary_taxable = Column(Integer, default=0)
    basic_salary_remarks = Column(String(100), nullable=True)

    # Private salary fields with 'private_' prefix
    private_allowances = Column(Integer, default=0)
    private_allowances_remarks = Column(String(100), nullable=True)
    private_arrear_salary = Column(Integer, default=0)
    private_arrear_salary_remarks = Column(String(100), nullable=True)
    private_gratuity = Column(Integer, default=0)
    private_gratuity_remarks = Column(String(100), nullable=True)
    private_perquisites = Column(Integer, default=0)
    private_perquisites_remarks = Column(String(100), nullable=True)
    private_receipts_or_additional_receipts_in_lieu_of_salary = Column(Integer, default=0)
    private_receipts_or_additional_receipts_in_lieu_of_salary_remarks = Column(String(100), nullable=True)
    private_income_from_employee_share_scheme = Column(Integer, default=0)
    private_income_from_employee_share_scheme_remarks = Column(String(100), nullable=True)
    private_housing_facility = Column(Integer, default=0)
    private_housing_facility_remarks = Column(String(100), nullable=True)
    private_vehicle_facility = Column(Integer, default=0)
    private_vehicle_facility_remarks = Column(String(100), nullable=True)
    private_any_other_benefit_provided_by_the_employer = Column(Integer, default=0)
    private_any_other_benefit_provided_by_the_employer_remarks = Column(String(100), nullable=True)
    private_contribution_paid_by_employer_to_recognized_pf = Column(Integer, default=0)
    private_contribution_paid_by_employer_to_recognized_pf_remarks = Column(String(100), nullable=True)
    private_others = Column(Integer, default=0)
    private_others_remarks = Column(String(100), nullable=True)

    # Government salary fields with 'gov_' prefix
    gov_arrear_pay = Column(Integer, default=0)
    gov_arrear_pay_exempted = Column(Integer, default=0)
    gov_arrear_pay_taxable = Column(Integer, default=0)
    gov_arrear_pay_remarks = Column(String, nullable=True)
    
    # Special Allowance
    gov_special_allowance = Column(Integer, default=0)
    gov_special_allowance_exempted = Column(Integer, default=0)
    gov_special_allowance_taxable = Column(Integer, default=0)
    gov_special_allowance_remarks = Column(String, nullable=True)
    
    # Medical Allowance
    gov_medical_allowance = Column(Integer, default=0)
    gov_medical_allowance_exempted = Column(Integer, default=0)
    gov_medical_allowance_taxable = Column(Integer, default=0)
    gov_medical_allowance_remarks = Column(String, nullable=True)
    
    # Conveyance Allowance
    gov_conveyance_allowance = Column(Integer, default=0)
    gov_conveyance_allowance_exempted = Column(Integer, default=0)
    gov_conveyance_allowance_taxable = Column(Integer, default=0)
    gov_conveyance_allowance_remarks = Column(String, nullable=True)

    # Festival Allowance
    gov_festival_allowance = Column(Integer, nullable=False, default=0)
    gov_festival_allowance_exempted = Column(Integer, default=0)
    gov_festival_allowance_taxable = Column(Integer, default=0)
    gov_festival_allowance_remarks = Column(String, nullable=True)
    
    # House Rent Allowance
    gov_house_rent_allowance = Column(Integer, default=0)
    gov_house_rent_allowance_exempted = Column(Integer, default=0)
    gov_house_rent_allowance_taxable = Column(Integer, default=0)
    gov_house_rent_allowance_remarks = Column(String, nullable=True)

    # Support Staff Allowance
    gov_support_staff_allowance = Column(Integer, default=0)
    gov_support_staff_allowance_exempted = Column(Integer, default=0)
    gov_support_staff_allowance_taxable = Column(Integer, default=0)
    gov_support_staff_allowance_remarks = Column(String, nullable=True)

    # Leave Allowance
    gov_leave_allowance = Column(Integer, default=0)
    gov_leave_allowance_exempted = Column(Integer, default=0)
    gov_leave_allowance_taxable = Column(Integer, default=0)
    gov_leave_allowance_remarks = Column(String, nullable=True)

    # Reward
    gov_reward = Column(Integer, default=0)
    gov_reward_exempted = Column(Integer, default=0)
    gov_reward_taxable = Column(Integer, default=0)
    gov_reward_remarks = Column(String, nullable=True)

    # Overtime
    gov_overtime = Column(Integer, default=0)
    gov_overtime_exempted = Column(Integer, default=0)
    gov_overtime_taxable = Column(Integer, default=0)
    gov_overtime_remarks = Column(String, nullable=True)

    # Bangla Noboborsho Allowance
    gov_bangla_noboborsho = Column(Integer, default=0)
    gov_bangla_noboborsho_exempted = Column(Integer, default=0)
    gov_bangla_noboborsho_taxable = Column(Integer, default=0)
    gov_bangla_noboborsho_remarks = Column(String, nullable=True)

    # Interest Accrued from Provident Fund (PF)
    gov_interest_accrued_from_PF = Column(Integer, default=0)
    gov_interest_accrued_from_PF_exempted = Column(Integer, default=0)
    gov_interest_accrued_from_PF_taxable = Column(Integer, default=0)
    gov_interest_accrued_from_PF_remarks = Column(String, nullable=True)

    # Lump Sum Grant
    gov_lump_grant = Column(Integer, default=0)
    gov_lump_grant_exempted = Column(Integer, default=0)
    gov_lump_grant_taxable = Column(Integer, default=0)
    gov_lump_grant_remarks = Column(String, nullable=True)

    # Gratuity
    gov_gratuity = Column(Integer, default=0)
    gov_gratuity_exempted = Column(Integer, default=0)
    gov_gratuity_taxable = Column(Integer, default=0)
    gov_gratuity_remarks = Column(String, nullable=True)

    # Other Allowances
    gov_others = Column(Integer, default=0)
    gov_others_exempted = Column(Integer, default=0)
    gov_others_taxable = Column(Integer, default=0)
    gov_others_remarks = Column(String, nullable=True)
    
    etin = Column(String(12), ForeignKey('taxpayer.etin'), nullable=False)
    employer_info_id = Column(Integer, ForeignKey('employer_info.id'), nullable=False)
    
    # Define a relationship to the Taxpayer table
    taxpayer = relationship("Taxpayer", back_populates="salary_income_records")    
    employer_info = relationship("EmployerInfo", back_populates="salary_income_records")
    # allowance_details = relationship("AllowanceDetails", back_populates="salary_income_records")
    # perquisite_details = relationship("PerquisiteDetails", back_populates="salary_income_records")
    # vehicle_facility_details = relationship("VehicleFacilityDetails", back_populates="salary_income_records")
    

    
class AllowanceDetails(Base):
    __tablename__ = "allowance_details"
    
    
    id = Column(Integer, primary_key=True, index=True, unique= True)
    any_allowance = Column(Integer, default=0)
    any_allowance_remarks = Column(String(100), nullable=True)
    leave_allowance = Column(Integer, default=0)
    leave_allowance_remarks = Column(String(100), nullable=True)
    lump_grant = Column(Integer, default=0)
    lump_grant_remarks = Column(String(100), nullable=True)
    bonus = Column(Integer, default=0)
    bonus_remarks = Column(String(100), nullable=True)
    fee = Column(Integer, default=0)
    fee_remarks = Column(String(100), nullable=True)
    commission = Column(Integer, default=0)
    commission_remarks = Column(String, nullable=True)
    overtime = Column(Integer, default=0)
    overtime_remarks = Column(String(100), nullable=True)
    other = Column(Integer, default=0)
    other_details = Column(String(100), nullable=True)
    total = Column(Integer, default=0 )
    
    etin = Column(String(12), ForeignKey('taxpayer.etin'), nullable=False)
    employer_info_id = Column(Integer, ForeignKey('employer_info.id'), nullable=False)
    
    
    taxpayer = relationship("Taxpayer", back_populates="allowance_details")
    employer_info = relationship("EmployerInfo", back_populates="allowance_details")
    
    
    
    
class PerquisiteDetails(Base):
    __tablename__ = 'perquisite_details'
    
    id = Column(Integer, primary_key=True, unique=True, index=True)
    mohargha_allowance = Column(Integer, default=0)
    mohargha_allowance_remarks = Column(String(100), nullable=True)
    insurance_premium_borne_by_the_employer = Column(Integer, default=0)
    insurance_premium_borne_by_the_employer_remarks = Column(String(100), nullable=True)
    housing_allowance = Column(Integer, default=0)
    housing_allowance_remarks = Column(String(100), nullable=True)
    house_rent_allowance = Column(Integer, default=0)
    house_rent_allowance_remarks = Column(String(100), nullable=True)
    entertainment_allowance = Column(Integer, default=0)
    entertainment_allowance_remarks = Column(String(100), nullable=True)
    transportation_allowance = Column(Integer, default=0)
    transportation_allowance_remarks = Column(String(100), nullable=True)
    passage_leave = Column(Integer, default=0)
    passage_leave_remarks = Column(String(100), nullable=True)
    medical_allowance = Column(Integer, default=0)
    medical_allowance_remarks = Column(String(100), nullable=True)
    any_other_obligations_of_the_employee = Column(Integer, default=0)
    any_other_obligations_of_the_employee_remarks = Column(String(100), nullable=True)
    other = Column(Integer, default=0)
    other_remarks = Column(String(100), nullable=True)
    total = Column(Integer, default=0)
    
    etin = Column(String(12), ForeignKey('taxpayer.etin'), nullable=False)
    employer_info_id = Column(Integer, ForeignKey('employer_info.id'), nullable=False)
    
    taxpayer = relationship("Taxpayer", back_populates="perquisite_details")
    employer_info = relationship("EmployerInfo", back_populates="perquisite_details")
    
    
    
class VehicleFacilityDetails(Base):
    __tablename__ = "vehicle_facility_details"  # Table name in the database

    
    id = Column(Integer, primary_key=True, index=True, unique=True)
    upto_2500CC = Column(String(100), nullable=False)  # Assuming this is a string (Y/N or description)
    cost_for_upto_2500 = Column(Integer, default=10000)  # Default value as provided
    greater_than_2500cc = Column(String(100), nullable=False)  # Assuming this is a string (Y/N or description)
    cost_for_more_than_2500 = Column(Integer, default=25000)  # Default value as provided
    no_of_months = Column(Integer, default=0)  # Default value as 0
    total = Column(Integer, default=0)  # Default value as 0
    
    etin = Column(String(12), ForeignKey('taxpayer.etin'), nullable=False)
    employer_info_id = Column(Integer, ForeignKey('employer_info.id'), nullable=False)
    
    taxpayer = relationship("Taxpayer", back_populates="vehicle_facility_details")
    employer_info = relationship("EmployerInfo", back_populates="vehicle_facility_details")
    
    
    

class SalaryIncomeSummary(Base):
    __tablename__ = "salary_income_summary"


    id = Column(Integer, primary_key=True, index=True, unique= True)
    total_income = Column(Integer, index= True, default= 0)
    exempted_income = Column(Integer, index= True, default= 0)
    taxable_income = Column(Integer, index= True, default= 0)
    tax_liability = Column(Integer, index= True, default= 0)
    
    etin = Column(String(12), ForeignKey('taxpayer.etin'), nullable=False)
    
    taxpayer = relationship("Taxpayer", back_populates="salary_income_summary")
    # rebate_record = relationship("RebateRecord", back_populates="salary_income_summary")
    
  
  
    
    
class FinancialAssetIncome(Base):
    __tablename__ = "financial_asset_income"
    id = Column(Integer, primary_key=True, autoincrement=True)

    savings_ban_interest_net_income = Column(Integer, default=0)
    savings_ban_interest_tax_deduction_at_source = Column(Integer, default=0)
    savings_ban_interest_interest_on_loans = Column(Integer, default=0)
    savings_ban_interest_allowable_expenditure = Column(Integer, default=0)
    savings_ban_interest_taxable = Column(Integer, default=0)
    savings_ban_interest_description = Column(String, nullable=True)

    other_securities_net_income = Column(Integer, default=0)
    other_securities_tax_deduction_at_source = Column(Integer, default=0)
    other_securities_interest_on_loans = Column(Integer, default=0)
    other_securities_allowable_expenditure = Column(Integer, default=0)
    other_securities_taxable = Column(Integer, default=0)
    other_securities_description = Column(String, nullable=True)

    income_from_islamic_principles_net_income = Column(Integer, default=0)
    income_from_islamic_principles_tax_deduction_at_source = Column(Integer, default=0)
    income_from_islamic_principles_interest_on_loans = Column(Integer, default=0)
    income_from_islamic_principles_allowable_expenditure = Column(Integer, default=0)
    income_from_islamic_principles_taxable = Column(Integer, default=0)
    income_from_islamic_principles_description = Column(String, nullable=True)

    bank_interest_savings_deposits_net_income = Column(Integer, default=0)
    bank_interest_savings_deposits_tax_deduction_at_source = Column(Integer, default=0)
    bank_interest_savings_deposits_interest_on_loans = Column(Integer, default=0)
    bank_interest_savings_deposits_allowable_expenditure = Column(Integer, default=0)
    bank_interest_savings_deposits_taxable = Column(Integer, default=0)
    bank_interest_savings_deposits_description = Column(String, nullable=True)

    fdr_interest_income_net_income = Column(Integer, default=0)
    fdr_interest_income_tax_deduction_at_source = Column(Integer, default=0)
    fdr_interest_income_interest_on_loans = Column(Integer, default=0)
    fdr_interest_income_allowable_expenditure = Column(Integer, default=0)
    fdr_interest_income_taxable = Column(Integer, default=0)
    fdr_interest_income_description = Column(String, nullable=True)

    dividend_income_net_income = Column(Integer, default=0)
    dividend_income_tax_deduction_at_source = Column(Integer, default=0)
    dividend_income_interest_on_loans = Column(Integer, default=0)
    dividend_income_allowable_expenditure = Column(Integer, default=0)
    dividend_income_taxable = Column(Integer, default=0)
    dividend_income_description = Column(String, nullable=True)
    
    
    total_net_income = Column(Integer, default=0)
    total_tax_deduction_at_source = Column(Integer, default=0)
    total_interest_on_loans = Column(Integer, default=0)
    total_allowable_expenditure = Column(Integer, default=0)
    total_taxable = Column(Integer, default=0)
    

    reduced_tax_rate_securities_net_income = Column(Integer, default=0)
    reduced_tax_rate_securities_tax_deduction_at_source = Column(Integer, default=0)
    reduced_tax_rate_securities_interest_on_loans = Column(Integer, default=0)
    reduced_tax_rate_securities_allowable_expenditure = Column(Integer, default=0)
    reduced_tax_rate_securities_taxable = Column(Integer, default=0)
    reduced_tax_rate_securities_description = Column(String, nullable=True)

    income_other_resources_net_income = Column(Integer, default=0)
    income_other_resources_tax_deduction_at_source = Column(Integer, default=0)
    income_other_resources_interest_on_loans = Column(Integer, default=0)
    income_other_resources_allowable_expenditure = Column(Integer, default=0)
    income_other_resources_taxable = Column(Integer, default=0)
    income_other_resources_description = Column(String, nullable=True)

    us_dollar_investment_bonds_net_income = Column(Integer, default=0)
    us_dollar_investment_bonds_tax_deduction_at_source = Column(Integer, default=0)
    us_dollar_investment_bonds_interest_on_loans = Column(Integer, default=0)
    us_dollar_investment_bonds_exampted_amount = Column(Integer, default=0)
    us_dollar_investment_bonds_allowable_expenditure = Column(Integer, default=0)
    us_dollar_investment_bonds_taxable = Column(Integer, default=0)
    us_dollar_investment_bonds_description = Column(String, nullable=True)

    euro_premium_bonds_net_income = Column(Integer, default=0)
    euro_premium_bonds_tax_deduction_at_source = Column(Integer, default=0)
    euro_premium_bonds_interest_on_loans = Column(Integer, default=0)
    euro_premium_bonds_exampted_amount = Column(Integer, default=0)
    euro_premium_bonds_allowable_expenditure = Column(Integer, default=0)
    euro_premium_bonds_taxable = Column(Integer, default=0)
    euro_premium_bonds_description = Column(String, nullable=True)

    pound_sterling_premium_bonds_net_income = Column(Integer, default=0)
    pound_sterling_premium_bonds_tax_deduction_at_source = Column(Integer, default=0)
    pound_sterling_premium_bonds_interest_on_loans = Column(Integer, default=0)
    pound_sterling_premium_bonds_exampted_amount = Column(Integer, default=0)
    pound_sterling_premium_bonds_allowable_expenditure = Column(Integer, default=0)
    pound_sterling_premium_bonds_taxable = Column(Integer, default=0)
    pound_sterling_premium_bonds_description = Column(String, nullable=True)

    us_dollar_premium_bonds_net_income = Column(Integer, default=0)
    us_dollar_premium_bonds_tax_deduction_at_source = Column(Integer, default=0)
    us_dollar_premium_bonds_interest_on_loans = Column(Integer, default=0)
    us_dollar_premium_bonds_exampted_amount = Column(Integer, default=0)
    us_dollar_premium_bonds_allowable_expenditure = Column(Integer, default=0)
    us_dollar_premium_bonds_taxable = Column(Integer, default=0)
    us_dollar_premium_bonds_description = Column(String, nullable=True)

    wage_earners_development_bonds_net_income = Column(Integer, default=0)
    wage_earners_development_bonds_tax_deduction_at_source = Column(Integer, default=0)
    wage_earners_development_bonds_interest_on_loans = Column(Integer, default=0)
    wage_earners_development_bonds_exampted_amount = Column(Integer, default=0)
    wage_earners_development_bonds_allowable_expenditure = Column(Integer, default=0)
    wage_earners_development_bonds_taxable = Column(Integer, default=0)
    wage_earners_development_bonds_description = Column(String, nullable=True)

    euro_investment_bonds_net_income = Column(Integer, default=0)
    euro_investment_bonds_tax_deduction_at_source = Column(Integer, default=0)
    euro_investment_bonds_interest_on_loans = Column(Integer, default=0)
    euro_investment_bonds_exampted_amount = Column(Integer, default=0)
    euro_investment_bonds_allowable_expenditure = Column(Integer, default=0)
    euro_investment_bonds_taxable = Column(Integer, default=0)
    euro_investment_bonds_description = Column(String, nullable=True)
    
    
    total_gross_income = Column(Integer, default=0) 
    total_gross_expense = Column(Integer, default=0) 
    total_gross_exampted = Column(Integer, default=0) 
    total_gross_taxable = Column(Integer, default=0) 
    
    etin = Column(String(12), ForeignKey('taxpayer.etin'), nullable=False)
    
    taxpayer = relationship("Taxpayer", back_populates="financial_asset_income")
    
    
    
    
class RentIncomeMaster(Base):
    __tablename__ = "rent_income_master"
    
    id = Column(Integer, primary_key=True, index=True, unique= True)
    area_type = Column(senum(AreaType), default=None)
    asset_name = Column(String(100), nullable=False)
    asset_address = Column(String(500), nullable=False)
    total_flats = Column(Integer, default=0)
    total_income = Column(Integer, default=0)
    total_expense = Column(Integer, default=0)
    special_income = Column(Integer, default=0)
    net_income = Column(Integer, default=0)
    rent_taken = Column(Integer, default=0)
    yearly_value = Column(Integer, default=0)
    total_adjusted_advance = Column(Integer, default=0)
    other_charge = Column(Integer, default=0)
    other_taken_rent = Column(Integer, default=0)
    vacancy_allowance = Column(Integer, default=0)
    insurance_premium_paid_actual = Column(Integer, default=0)
    insurance_premium_paid_allowable = Column(Integer, default=0)
    interest_on_repaid_loans_actual = Column(Integer, default=0)
    interest_on_repaid_loans_allowable = Column(Integer, default=0)
    land_revenue_actual = Column(Integer, default=0)
    land_revenue_allowable = Column(Integer, default=0)
    municipal_or_local_tax_actual = Column(Integer, default=0)
    municipal_or_local_tax_allowable = Column(Integer, default=0)
    receipt_of_repairs_actual = Column(Integer, default=0)
    receipt_of_repairs_allowable = Column(Integer, default=0)
     
    
    etin = Column(String(12), ForeignKey('taxpayer.etin'), nullable=False)
    
    taxpayer = relationship("Taxpayer", back_populates="rent_income_master")
    rent_income_details = relationship("RentIncomeDetails", back_populates="rent_income_master")
    
 
 
class RentIncomeDetails(Base):
    __tablename__ = "rent_income_details"
 
    
    id = Column(Integer, primary_key=True, index=True, unique= True)
    space_type = Column(String(100), nullable=False)
    live_ownself = Column(senum(LiveOwnself), default=None) 
    monthly_rent = Column(Integer, default=0)
    monthly_service_charge = Column(Integer, default=0)  
    advance = Column(Integer, default=0)
    adjusted_rent = Column(Integer, default=0)
    all_month = Column(senum(Months), default=None)
    january = Column(senum(Months), default=None)
    february = Column(senum(Months), default=None)
    march = Column(senum(Months), default=None)
    april = Column(senum(Months), default=None)
    may = Column(senum(Months), default=None)
    june = Column(senum(Months), default=None) 
    july = Column(senum(Months), default=None)
    august = Column(senum(Months), default=None)
    september = Column(senum(Months), default=None)
    october = Column(senum(Months), default=None)
    november = Column(senum(Months), default=None)
    december = Column(senum(Months), default=None)
    total_rent = Column(Integer, default=0)
    total_rent_received = Column(Integer, default=0)
    total_service_charge_received = Column(Integer, default=0)
    total_vacancy_rent = Column(Integer, default=0)
    total_vacancy_month = Column(Integer, default=0)
    adjusted_advance = Column(Integer, default=0)
    
    master_id = Column(Integer, ForeignKey('rent_income_master.id'), nullable=False)
    etin = Column(String(12), ForeignKey('taxpayer.etin'), nullable=False)
    
    taxpayer = relationship("Taxpayer", back_populates="rent_income_details")
    rent_income_master = relationship("RentIncomeMaster", back_populates="rent_income_details")
 
    
class RentIncomeSummary(Base):
    __tablename__ = "rent_income_summary"
    
    
    id = Column(Integer, primary_key=True, index=True, unique= True)
    gross_total_income = Column(Integer, default=0)
    gross_total_expense = Column(Integer, default=0)
    gross_net_income = Column(Integer, default=0)
    
    etin = Column(String(12), ForeignKey('taxpayer.etin'), nullable=False)
    
    taxpayer = relationship("Taxpayer", back_populates="rent_income_summary")
    
    
    
    
    
class InvestmentRecord(Base):
    __tablename__ = "investment_record"
    
    
    id = Column(Integer, primary_key=True, index=True, unique= True)
    gov_securities_actual = Column(Integer, default=0)
    gov_securities_allowable = Column(Integer, default=0)
    gov_securities_remarks = Column(String, nullable=True)

    eft_actual = Column(Integer, default=0)
    eft_allowable = Column(Integer, default=0)
    eft_remarks = Column(String, nullable=True)
    
    life_insurance_given_premium_actual = Column(Integer, default=0)
    life_insurance_given_premium_allowable = Column(Integer, default=0)
    life_insurance_given_premium_remarks = Column(String, nullable=True)

    contribution_paid_to_deposit_pension_actual = Column(Integer, default=0)
    contribution_paid_to_deposit_pension_allowable = Column(Integer, default=0)
    contribution_paid_to_deposit_pension_remarks = Column(String, nullable=True)

    investment_in_any_securities_actual = Column(Integer, default=0)
    investment_in_any_securities_allowable = Column(Integer, default=0)
    investment_in_any_securities_remarks = Column(String, nullable=True)

    provisions_of_pf_act_1925_actual = Column(Integer, default=0)
    provisions_of_pf_act_1925_allowable = Column(Integer, default=0)
    provisions_of_pf_act_1925_remarks = Column(String, nullable=True)

    contributions_to_approved_provident_fund_actual = Column(Integer, default=0)
    contributions_to_approved_provident_fund_allowable = Column(Integer, default=0)
    contributions_to_approved_provident_fund_remarks = Column(String, nullable=True)

    contributions_to_superannuation_funds_actual = Column(Integer, default=0)
    contributions_to_superannuation_funds_allowable = Column(Integer, default=0)
    contributions_to_superannuation_funds_remarks = Column(String, nullable=True)

    contribution_to_welfare_fund_actual = Column(Integer, default=0)
    contribution_to_welfare_fund_allowable = Column(Integer, default=0)
    contribution_to_welfare_fund_remarks = Column(String, nullable=True)

    contribution_to_zakat_fund_actual = Column(Integer, default=0)
    contribution_to_zakat_fund_allowable = Column(Integer, default=0)
    contribution_to_zakat_fund_remarks = Column(String, nullable=True)

    donation_to_liberation_war_memory_actual = Column(Integer, default=0)
    donation_to_liberation_war_memory_allowable = Column(Integer, default=0)
    donation_to_liberation_war_memory_remarks = Column(String, nullable=True)

    donations_to_father_of_nation_memory_actual = Column(Integer, default=0)
    donations_to_father_of_nation_memory_allowable = Column(Integer, default=0)
    donations_to_father_of_nation_memory_remarks = Column(String, nullable=True)

    donation_to_disabled_organizations_actual = Column(Integer, default=0)
    donation_to_disabled_organizations_allowable = Column(Integer, default=0)
    donation_to_disabled_organizations_remarks = Column(String, nullable=True)

    donations_to_liberation_war_museum_actual = Column(Integer, default=0)
    donations_to_liberation_war_museum_allowable = Column(Integer, default=0)
    donations_to_liberation_war_museum_remarks = Column(String, nullable=True)

    donation_to_ahsania_cancer_hospital_actual = Column(Integer, default=0)
    donation_to_ahsania_cancer_hospital_allowable = Column(Integer, default=0)
    donation_to_ahsania_cancer_hospital_remarks = Column(String, nullable=True)

    donations_to_icddrb_actual = Column(Integer, default=0)
    donations_to_icddrb_allowable = Column(Integer, default=0)
    donations_to_icddrb_remarks = Column(String, nullable=True)

    donation_to_crp_savar_actual = Column(Integer, default=0)
    donation_to_crp_savar_allowable = Column(Integer, default=0)
    donation_to_crp_savar_remarks = Column(String, nullable=True)

    donations_to_charitable_educational_institutions_actual = Column(Integer, default=0)
    donations_to_charitable_educational_institutions_allowable = Column(Integer, default=0)
    donations_to_charitable_educational_institutions_remarks = Column(String, nullable=True)

    donation_to_asiatic_society_actual = Column(Integer, default=0)
    donation_to_asiatic_society_allowable = Column(Integer, default=0)
    donation_to_asiatic_society_remarks = Column(String, nullable=True)

    donation_to_dhaka_ahsania_mission_actual = Column(Integer, default=0)
    donation_to_dhaka_ahsania_mission_allowable = Column(Integer, default=0)
    donation_to_dhaka_ahsania_mission_remarks = Column(String, nullable=True)

    contribution_to_super_annuity_fund_actual = Column(Integer, default=0)
    contribution_to_super_annuity_fund_allowable = Column(Integer, default=0)
    contribution_to_super_annuity_fund_remarks = Column(String, nullable=True)

    other_actual = Column(Integer, default=0)
    other_allowable = Column(Integer, default=0)
    other_remarks = Column(String, nullable=True)
    
    total_investment = Column(Integer, default=0)
    allowable_investment = Column(Integer, default=0)
    
    
    etin = Column(String(12), ForeignKey('taxpayer.etin'), nullable=False)
    
    taxpayer = relationship("Taxpayer", back_populates="investment_record")
    # rebate_record = relationship("RebateRecord", back_populates="investment_record")
    
    
class GivenPremium(Base):
    __tablename__ = "given_premium"
    
    
    
    id = Column(Integer, primary_key=True, index=True, unique= True)
    policy_no = Column(String(100), index= True, nullable= True)
    company = Column(String(100), index= True, nullable= True)
    policy_value = Column(Integer, index= True, default= 0)
    given_premium = Column(Integer, index= True, default= 0)
    allowable = Column(Integer, index= True, default= 0)
    remarks = Column(String(100), index= True, nullable= True)
    
    etin = Column(String(12), ForeignKey('taxpayer.etin'), nullable=False)
    
    taxpayer = relationship("Taxpayer", back_populates="given_premium")
    
    # investment_id = Column(Integer, ForeignKey('investment_record.id'), nullable=False)

    # investment_record = relationship("InvestmentRecord", back_populates="given_premium")
    
    
class GovSecurities(Base):
    __tablename__ = "gov_securities"
    
    
    id = Column(Integer, primary_key=True, index=True, unique= True)
    description = Column(String(100), index= True, nullable= True)
    actual = Column(Integer, index= True, default= 0)
    allowable = Column(Integer, index= True, default= 0)
    
    etin = Column(String(12), ForeignKey('taxpayer.etin'), nullable=False)
    
    taxpayer = relationship("Taxpayer", back_populates="gov_securities")
    
    # investment_id = Column(Integer, ForeignKey('investment_record.id'), nullable=False)

    # investment_record = relationship("InvestmentRecord", back_populates="gov_securities")    
    
    
    
class EFT(Base):
    __tablename__ = "eft"
    
    
    id = Column(Integer, primary_key=True, index=True, unique= True)
    description = Column(String(100), index= True, nullable= True)
    actual = Column(Integer, index= True, default= 0)
    allowable = Column(Integer, index= True, default= 0)
    
    etin = Column(String(12), ForeignKey('taxpayer.etin'), nullable=False)
    
    taxpayer = relationship("Taxpayer", back_populates="eft")
    
    # investment_id = Column(Integer, ForeignKey('investment_record.id'), nullable=False)

    # investment_record = relationship("InvestmentRecord", back_populates="eft")    
    
    
    
    
class DPS(Base):
    __tablename__ = "dps"
    
    
    id = Column(Integer, primary_key=True, index=True, unique= True)
    description = Column(String(100), index= True, nullable= True)
    actual = Column(Integer, index= True, default= 0)
    allowable = Column(Integer, index= True, default= 0)
    
    etin = Column(String(12), ForeignKey('taxpayer.etin'), nullable=False)
    
    taxpayer = relationship("Taxpayer", back_populates="dps")
    
    # investment_id = Column(Integer, ForeignKey('investment_record.id'), nullable=False)

    # investment_record = relationship("InvestmentRecord", back_populates="dps")    
    

    
    
class RebateRecord(Base):
    __tablename__ = "rebate_record"
    
    
    id = Column(Integer, primary_key=True, index=True, unique= True)
    taxable_income = Column(Integer,  default=0, nullable=False)
    allowable_investment = Column(Integer, default=0, nullable=False)
    
    
    etin = Column(String(12), ForeignKey('taxpayer.etin'), nullable=False)

    
    rebate = Column(Integer, index= True, default= 0)
    
    taxpayer = relationship("Taxpayer", back_populates="rebate_record")
    # salary_income_summary = relationship("SalaryIncomeSummary", back_populates="rebate_record")
    # investment_record = relationship("InvestmentRecord", back_populates="rebate_record")
    
    
    
    
class TaxRecord(Base):
    __tablename__ = "tax"
    
    
    id = Column(Integer, primary_key=True, index=True, unique= True)
    etin = Column(String(12), ForeignKey('taxpayer.etin'), nullable=False)
    net_tax_liability = Column(Integer, index= True, default= 0)
    min_tax = Column(Integer, index= True, default= 0)
    area_tax = Column(Integer, index= True, default= 0)
    actual_payable_tax = Column(Integer, index= True, default= 0)
    
    
    taxpayer = relationship("Taxpayer", back_populates="tax")
    
    