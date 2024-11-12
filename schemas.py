from pydantic import BaseModel
from models import *


class TaxPayers(BaseModel):
    name: str
    nid : str
    etin : str
    circle : str
    zone : str
    assesment_year : str
    residential_status : ResidentialStatus
    gender : Gender
    employment_type : EmploymentType
    company_name : str
    freedom_fighter : FreedomFighter
    disable : Disable
    parent_of_disable : ParentOfDisable
    num_autistic_children : int
    age_above_65 : AgeAbove65
    date_of_birth : str
    spouse_name : str
    spouse_tin : str | None = None
    address : str
    telephone : str | None = None
    mobile : str
    email : str
    employer_name : str
    name_of_organization : str
    bin_no : str
    name_tin_partners : str |None = None 
    
    class Config:
        orm_mode = True
    

class TaxPayerCreate(TaxPayers):
    pass




class SalaryIncomeRecord(BaseModel):
    etin : str
    basic_salary: int
    house_rent_allowance: int
    medical_allowance: int
    conveyance_allowance: int 
    festival_bonus: int
    

    class Config:
        orm_mode = True


class PrivateSalary_IncomeRecord(SalaryIncomeRecord):
    rent_free_accommodation: int = 0
    accommodation_at_concessional_rate: int = 0
    rent_paid_by_taxpayer: int = 0
    vehicle_facility_months: int = 0
    is_higher_cc: str = 'No'  # 'Yes' or 'No'
    other_non_cash_benefits: int = 0  # Store as JSON (stringified dict)
    num_autistic_children: int = 0
    arrear_salary: int = 0
    education_allowance: int = 0
    entertainment_allowance: int = 0
    employer_contribution_RPF: int = 0
    gratuity: int = 0
    interest_accrued_RPF: int = 0
    leave_allowance: int = 0
    other_bonus: int = 0
    overtime_bonus: int = 0
    pension: int = 0
    tada: int = 0
    income_from_employee_share_scheme: int = 0
    others: int = 0
    fee: int = 0
    mohargha_allowance : int = 0
    commission : int = 0
    allowances: int = 0
    perquisites: int = 0
    
    
    
class GovSalary_IncomeRecord(SalaryIncomeRecord):
    arrear_pay: int = 0
    special_allowance: int = 0
    support_staff_allowance: int = 0
    leave_allowance: int = 0
    reward: int = 0
    overtime: int = 0
    bangla_noboborsho: int = 0
    interest_accrued_from_PF: int = 0
    lump_grant: int = 0
    gratuity: int = 0
    others: int = 0
    
    
    
class SalaryIncome_Summary(BaseModel):
    etin : str
    total_income : int
    exempted_income : int
    taxable_income : int
    tax_liability : int
    
    class Config:
        orm_mode = True