from pydantic import BaseModel, EmailStr
from models import *
from typing import Optional


class User_Auth(BaseModel):
    username : str
    email : EmailStr
    password : str
    
    class Config:
        orm_mode = True


class TaxPayers(BaseModel): 
    # user_id : int
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
    email : EmailStr
    employer_name : str
    name_of_organization : str
    bin_no : str
    name_tin_partners : str |None = None
    
    class Config:
        orm_mode = True
    

class TaxPayerCreate(TaxPayers):
    pass




class Employer_info(BaseModel):
    name : str
    start_date : str
    end_date : str

    class Config:
        orm_mode = True



class SalaryIncome_Record(BaseModel):
    etin: str
    employer_info_id : int
    
    basic_salary: int
    basic_salary_exempted: int
    basic_salary_taxable: int
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
    # Arrear Pay
    gov_arrear_pay: int
    gov_arrear_pay_exempted: int
    gov_arrear_pay_taxable: int
    gov_arrear_pay_remarks: Optional[str]

    # Special Allowance
    gov_special_allowance: int = 0
    gov_special_allowance_exempted: int = 0
    gov_special_allowance_taxable: int = 0
    gov_special_allowance_remarks: Optional[str] = None

    # Medical Allowance
    gov_medical_allowance: int = 0
    gov_medical_allowance_exempted: int = 0
    gov_medical_allowance_taxable: int = 0
    gov_medical_allowance_remarks: Optional[str] = None

    # Conveyance Allowance
    gov_conveyance_allowance: int = 0
    gov_conveyance_allowance_exempted: int = 0
    gov_conveyance_allowance_taxable: int = 0
    gov_conveyance_allowance_remarks: Optional[str] = None

    # Festival Allowance
    gov_festival_allowance: int = 0
    gov_festival_allowance_exempted: int = 0
    gov_festival_allowance_taxable: int = 0
    gov_festival_allowance_remarks: Optional[str] = None

    # House Rent Allowance
    gov_house_rent_allowance: int = 0
    gov_house_rent_allowance_exempted: int = 0
    gov_house_rent_allowance_taxable: int = 0
    gov_house_rent_allowance_remarks: Optional[str] = None

    # Support Staff Allowance
    gov_support_staff_allowance: int
    gov_support_staff_allowance_exempted: int
    gov_support_staff_allowance_taxable: int
    gov_support_staff_allowance_remarks: Optional[str]

    # Leave Allowance
    gov_leave_allowance: int
    gov_leave_allowance_exempted: int
    gov_leave_allowance_taxable: int
    gov_leave_allowance_remarks: Optional[str]

    # Reward
    gov_reward: int
    gov_reward_exempted: int
    gov_reward_taxable: int
    gov_reward_remarks: Optional[str]

    # Overtime
    gov_overtime: int
    gov_overtime_exempted: int
    gov_overtime_taxable: int
    gov_overtime_remarks: Optional[str]

    # Bangla Noboborsho Allowance
    gov_bangla_noboborsho: int
    gov_bangla_noboborsho_exempted: int
    gov_bangla_noboborsho_taxable: int
    gov_bangla_noboborsho_remarks: Optional[str]

    # Interest Accrued from Provident Fund (PF)
    gov_interest_accrued_from_PF: int
    gov_interest_accrued_from_PF_exempted: int
    gov_interest_accrued_from_PF_taxable: int
    gov_interest_accrued_from_PF_remarks: Optional[str]

    # Lump Sum Grant
    gov_lump_grant: int
    gov_lump_grant_exempted: int
    gov_lump_grant_taxable: int
    gov_lump_grant_remarks: Optional[str]

    # Gratuity
    gov_gratuity: int
    gov_gratuity_exempted: int
    gov_gratuity_taxable: int
    gov_gratuity_remarks: Optional[str]

    # Other Allowances
    gov_others: int
    gov_others_exempted: int
    gov_others_taxable: int
    gov_others_remarks: Optional[str]

    class Config:
        orm_mode = True




class Allowance_Details(BaseModel):
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
    
    def __init__(self, **data):
        super().__init__(**data)
        self.total = (
            self.any_allowance +
            self.leave_allowance +
            self.lump_grant +
            self.bonus +
            self.fee +
            self.commission +
            self.overtime +
            self.other
        )
        
    class Config:
            orm_mode = True




class Perquisite_Details(BaseModel):
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
    
    def __init__(self, **data):
        super().__init__(**data)
        self.total = (
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
    
    class Config:
            orm_mode = True
            
            

class Vehicale_facility_Details(BaseModel):
    upto_2500CC : str = "No"
    cost_for_upto_2500 : int = 10000
    greater_than_2500cc : str = "No"
    cost_for_more_than_2500 : int = 25000
    no_of_months : int = 0
    total : int = 0  
    
    def __init__(self, **data):
        super().__init__(**data)
        self.total = (
            (self.cost_for_upto_2500 if self.upto_2500CC.upper() == "YES" else 0) +
            (self.cost_for_more_than_2500 if self.greater_than_2500cc.upper() == "YES" else 0)
        ) * self.no_of_months
    
    class Config:
        orm_mode = True

    
    
    
class SalaryIncome_Summary(BaseModel):
    total_income : int
    exempted_income : int
    taxable_income : int
    tax_liability : int
    
    class Config:
        orm_mode = True
        
        
        
        
class Investment_Record(BaseModel):
    gov_securities_actual: int = 0
    gov_securities_allowable: int = 0
    gov_securities_remarks: Optional[str] = None

    eft_actual: int = 0
    eft_allowable: int = 0
    eft_remarks: Optional[str] = None
    
    life_insurance_given_premium_actual: int = 0
    life_insurance_given_premium_allowable: int = 0
    life_insurance_given_premium_remarks: Optional[str] = None

    # premium_or_contractual_deferred_annuity_actual: int = 0
    # premium_or_contractual_deferred_annuity_allowable: int = 0
    # premium_or_contractual_deferred_annuity_remarks: Optional[str] = None

    contribution_paid_to_deposit_pension_actual: int = 0
    contribution_paid_to_deposit_pension_allowable: int = 0
    contribution_paid_to_deposit_pension_remarks: Optional[str] = None

    investment_in_any_securities_actual: int = 0
    investment_in_any_securities_allowable: int = 0
    investment_in_any_securities_remarks: Optional[str] = None

    provisions_of_pf_act_1925_actual: int = 0
    provisions_of_pf_act_1925_allowable: int = 0
    provisions_of_pf_act_1925_remarks: Optional[str] = None

    contributions_to_approved_provident_fund_actual: int = 0
    contributions_to_approved_provident_fund_allowable: int = 0
    contributions_to_approved_provident_fund_remarks: Optional[str] = None

    contributions_to_superannuation_funds_actual: int = 0
    contributions_to_superannuation_funds_allowable: int = 0
    contributions_to_superannuation_funds_remarks: Optional[str] = None

    contribution_to_welfare_fund_actual: int = 0
    contribution_to_welfare_fund_allowable: int = 0
    contribution_to_welfare_fund_remarks: Optional[str] = None

    contribution_to_zakat_fund_actual: int = 0
    contribution_to_zakat_fund_allowable: int = 0
    contribution_to_zakat_fund_remarks: Optional[str] = None

    donation_to_liberation_war_memory_actual: int = 0
    donation_to_liberation_war_memory_allowable: int = 0
    donation_to_liberation_war_memory_remarks: Optional[str] = None

    donations_to_father_of_nation_memory_actual: int = 0
    donations_to_father_of_nation_memory_allowable: int = 0
    donations_to_father_of_nation_memory_remarks: Optional[str] = None

    donation_to_disabled_organizations_actual: int = 0
    donation_to_disabled_organizations_allowable: int = 0
    donation_to_disabled_organizations_remarks: Optional[str] = None

    donations_to_liberation_war_museum_actual: int = 0
    donations_to_liberation_war_museum_allowable: int = 0
    donations_to_liberation_war_museum_remarks: Optional[str] = None

    donation_to_ahsania_cancer_hospital_actual: int = 0
    donation_to_ahsania_cancer_hospital_allowable: int = 0
    donation_to_ahsania_cancer_hospital_remarks: Optional[str] = None

    donations_to_icddrb_actual: int = 0
    donations_to_icddrb_allowable: int = 0
    donations_to_icddrb_remarks: Optional[str] = None

    donation_to_crp_savar_actual: int = 0
    donation_to_crp_savar_allowable: int = 0
    donation_to_crp_savar_remarks: Optional[str] = None

    donations_to_charitable_educational_institutions_actual: int = 0
    donations_to_charitable_educational_institutions_allowable: int = 0
    donations_to_charitable_educational_institutions_remarks: Optional[str] = None

    donation_to_asiatic_society_actual: int = 0
    donation_to_asiatic_society_allowable: int = 0
    donation_to_asiatic_society_remarks: Optional[str] = None

    donation_to_dhaka_ahsania_mission_actual: int = 0
    donation_to_dhaka_ahsania_mission_allowable: int = 0
    donation_to_dhaka_ahsania_mission_remarks: Optional[str] = None

    contribution_to_super_annuity_fund_actual: int = 0
    contribution_to_super_annuity_fund_allowable: int = 0
    contribution_to_super_annuity_fund_remarks: Optional[str] = None

    other_actual: int = 0
    other_allowable: int = 0
    other_remarks: Optional[str] = None
    
    total_investment : int = 0
    allowable_investment : int = 0
    

    class Config:
        orm_mode = True
        
        
        
        
class Given_Premium(BaseModel):
    policy_no : Optional[str] = None
    company : Optional[str] = None
    policy_value : int = 0
    given_premium : int = 0
    allowable : int = 0
    remarks : Optional[str] = None
    
    def __init__(self, **data):
        super().__init__(**data)
        # Calculate allowable as the minimum of actual and 120000
        self.allowable = min(self.given_premium * 0.1, self.policy_value)
    
    class Config:
        orm_mode = True
        
        
        
        
class Gov_Securities(BaseModel):
    description : Optional[str] = None
    actual : int = 0
    allowable : int =0
    
    def __init__(self, **data):
        super().__init__(**data)
        # Calculate allowable as the minimum of actual and 120000
        self.allowable = min(self.actual, 500000)
    
    class Config:
        orm_mode = True   
        
        
        
        
class E_FT(BaseModel):
    description : Optional[str] = None
    actual : int = 0
    allowable : int =0
    
    def __init__(self, **data):
        super().__init__(**data)
        # Calculate allowable as the minimum of actual and 120000
        self.allowable = min(self.actual, 500000)
    
    
    class Config:
        orm_mode = True
        
        
class D_PS(BaseModel):
    description : Optional[str] = None
    actual : int = 0
    allowable : int =0
    
    def __init__(self, **data):
        super().__init__(**data)
        # Calculate allowable as the minimum of actual and 120000
        self.allowable = min(self.actual, 120000)
    
    class Config:
        orm_mode = True 
        
        
class Rebate_Record(BaseModel):
    taxable_income : int = 0
    allowable_investment : int = 0
    rebate : int = 0
    
    class Config:
        orm_mode = True
        
        
class Tax_Record(BaseModel):
    net_tax_liability : int = 0
    area_tax : int = 0
    actual_payable_tax : int = 0
    
    class Config:
        orm_mode = True
        
        
        
        

        