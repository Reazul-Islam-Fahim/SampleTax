from pydantic import BaseModel
from models import *
from typing import Optional


class User_Auth(BaseModel):
    username : str
    email : str
    password : str
    
    class config:
        orm_mode = True


class TaxPayers(BaseModel): 
    user_id : int
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




class Employer_info(BaseModel):
    etin:str
    name : str
    start_date : str
    end_date : str

    class config:
        orm_mode = True



class SalaryIncome_Record(BaseModel):
    etin: str
    basic_salary: int
    basic_salary_remarks : Optional[str] = None
      
    
    # Private salary fields
    private_allowances: int = 0
    private_allowances_remarks: Optional[str] = None
    private_arrear_salary: int = 0
    private_arrear_salary_remarks: Optional[str] = None
    private_gratuity: int = 0
    private_gratuity_remarks: Optional[str] = None
    private_perquisites: int = 0
    private_perquisites_remarks: Optional[str] = None
    private_receipts_or_additional_receipts_in_lieu_of_salary: int = 0
    private_receipts_or_additional_receipts_in_lieu_of_salary_remarks: Optional[str] = None
    private_income_from_employee_share_scheme: int = 0
    private_income_from_employee_share_scheme_remarks: Optional[str] = None
    private_housing_facility: int = 0
    private_housing_facility_remarks: Optional[str] = None
    private_vehicle_facility: int = 0
    private_vehicle_facility_remarks: Optional[str] = None
    private_any_other_benefit_provided_by_the_employer: int = 0
    private_any_other_benefit_provided_by_the_employer_remarks: Optional[str] = None
    private_contribution_paid_by_employer_to_recognized_pf: int = 0
    private_contribution_paid_by_employer_to_recognized_pf_remarks: Optional[str] = None
    private_others: int = 0
    private_others_remarks: Optional[str] = None

    # Government salary fields with 'gov_' prefix
    gov_arrear_pay: int = 0
    gov_arrear_pay_remarks: Optional[str] = None
    gov_festival_allowance: int = 0
    gov_festival_allowance_remarks: Optional[str] = None
    gov_special_allowance: int = 0
    gov_special_allowance_remarks: Optional[str] = None
    gov_support_staff_allowance: int = 0
    gov_support_staff_allowance_remarks: Optional[str] = None
    gov_leave_allowance: int = 0
    gov_leave_allowance_remarks: Optional[str] = None
    gov_reward: int = 0
    gov_reward_remarks: Optional[str] = None
    gov_overtime: int = 0
    gov_overtime_remarks: Optional[str] = None
    gov_bangla_noboborsho: int = 0
    gov_bangla_noboborsho_remarks: Optional[str] = None
    gov_interest_accrued_from_PF: int = 0
    gov_interest_accrued_from_PF_remarks: Optional[str] = None
    gov_lump_grant: int = 0
    gov_lump_grant_remarks: Optional[str] = None
    gov_gratuity: int = 0
    gov_gratuity_remarks: Optional[str] = None
    gov_others: int = 0
    gov_others_remarks: Optional[str] = None

    class Config:
        orm_mode = True




class Allowance_Details(BaseModel):
    etin : str
    any_allowance: int = 0
    any_allowance_remarks: Optional[str] = None
    leave_allowance: int = 0
    leave_allowance_remarks: Optional[str] = None
    lump_grant: int = 0
    lump_grant_remarks: Optional[str] = None
    bonus: int = 0
    bonus_remarks: Optional[str] = None
    fee: int = 0
    fee_remarks: Optional[str] = None
    commission: int = 0
    commission_remarks: Optional[str] = None
    overtime: int = 0
    overtime_remarks: Optional[str] = None
    other: int = 0
    other_details: Optional[str] = None
    total : int = 0
    
    @property
    def total(self):
        # Calculate the total dynamically
        return (
            self.any_allowance +
            self.leave_allowance +
            self.lump_grant +
            self.bonus +
            self.fee +
            self.commission +
            self.overtime +
            self.other
        )

    class config:
            orm_mode = True




class Perquisite_Details(BaseModel):
    etin : str
    mohargha_allowance: int = 0
    mohargha_allowance_remarks: Optional[str] = None
    insurance_premium_borne_by_the_employer: int = 0
    insurance_premium_borne_by_the_employer_remarks: Optional[str] = None
    housing_allowance: int = 0
    housing_allowance_remarks: Optional[str] = None
    house_rent_allowance: int = 0
    house_rent_allowance_remarks: Optional[str] = None
    entertainment_allowance: int = 0
    entertainment_allowance_remarks: Optional[str] = None
    passage_leave: int = 0
    passage_leave_remarks: Optional[str] = None
    medical_allowance: int = 0
    medical_allowance_remarks: Optional[str] = None
    any_other_obligations_of_the_employee: int = 0
    any_other_obligations_of_the_employee_remarks: Optional[str] = None
    other: int = 0
    other_remarks: Optional[str] = None
    total : int = 0
    
    @property
    def total(self):
        return (
            self.mohargha_allowance +
            self.insurance_premium_borne_by_the_employer +
            self.housing_allowance +
            self.house_rent_allowance +
            self.entertainment_allowance +
            self.passage_leave +
            self.medical_allowance +
            self.any_other_obligations_of_the_employee +
            self.other
        )
    
    class config:
            orm_mode = True
            
            

class Vehicale_facility_Details(BaseModel):
    etin : str
    upto_2500CC : str
    cost_for_upto_2500 : int = 10000
    greater_than_2500cc : str
    cost_for_more_than_2500 : int = 25000
    no_of_months : int = 0
    total : int = 0  
    
    class config:
        orm_mode = True

    
    
    
class SalaryIncome_Summary(BaseModel):
    etin : str
    total_income : int
    exempted_income : int
    taxable_income : int
    tax_liability : int
    
    class Config:
        orm_mode = True
        
        
        
        
class Investment_Record(BaseModel):
    etin: str
    gov_securities : int = 0
    eft : int = 0
    life_insurance_policy_value : int = 0
    life_insurance_given_premium : int = 0
    other : int = 0  
      
    class Config:
        orm_mode = True
        
        
class Rebate_Record(BaseModel):
    etin : str
    actual_investment : int = 0
    allowable_investment : int = 0
    rebate : int = 0
    
    class config:
        orm_mode = True
        
        
        

        