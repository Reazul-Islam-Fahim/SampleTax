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
    gov_securities: int = 0
    gov_securities_remarks: Optional[str] = None
    eft: int = 0
    eft_remarks: Optional[str] = None
    life_insurance_policy_value: int = 0
    life_insurance_policy_value_remarks: Optional[str] = None
    life_insurance_given_premium: int = 0
    life_insurance_given_premium_remarks: Optional[str] = None
    premium_or_contractual_deferred_annuity_of_life_insurance_policy_paid_in_Bangladesh: int = 0
    premium_or_contractual_deferred_annuity_of_life_insurance_policy_paid_in_Bangladesh_remarks: Optional[str] = None
    contribution_paid_to_deposit_pension_or_monthly_savings_scheme: int = 0
    contribution_paid_to_deposit_pension_or_monthly_savings_scheme_remarks: Optional[str] = None
    investment_in_any_securities_listed_with_an_authorized_stock_exchange: int = 0
    investment_in_any_securities_listed_with_an_authorized_stock_exchange_remarks: Optional[str] = None
    provisions_of_pf_Act_1925_apply_to_the_contribution_of_the_taxpayer_to_any_such_fund: int = 0
    provisions_of_pf_Act_1925_apply_to_the_contribution_of_the_taxpayer_to_any_such_fund_remarks: Optional[str] = None
    contributions_made_by_the_taxpayer_and_his_employer_to_an_approved_provident_fund: int = 0
    contributions_made_by_the_taxpayer_and_his_employer_to_an_approved_provident_fund_remarks: Optional[str] = None
    contributions_paid_to_approved_superannuation_funds: int = 0
    contributions_paid_to_approved_superannuation_funds_remarks: Optional[str] = None
    contribution_paid_to_welfare_fund_group_insurance_fund: int = 0
    contribution_paid_to_welfare_fund_group_insurance_fund_remarks: Optional[str] = None
    contribution_paid_to_zakat_fund: int = 0
    contribution_paid_to_zakat_fund_remarks: Optional[str] = None
    donation_to_any_national_level_institution_dedicated_to_the_preservation_of_the_memory_of_the_liberation_war: int = 0
    donation_to_any_national_level_institution_dedicated_to_the_preservation_of_the_memory_of_the_liberation_war_remarks: Optional[str] = None
    donations_to_national_institutions_to_preserve_the_memory_of_the_father_of_the_nation: int = 0
    donations_to_national_institutions_to_preserve_the_memory_of_the_father_of_the_nation_remarks: Optional[str] = None
    donation_to_organizations_established_for_the_welfare_of_the_disabled: int = 0
    donation_to_organizations_established_for_the_welfare_of_the_disabled_remarks: Optional[str] = None
    donations_made_to_the_liberation_war_museum: int = 0
    donations_made_to_the_liberation_war_museum_remarks: Optional[str] = None
    donation_to_ahsania_cancer_hospital: int = 0
    donation_to_ahsania_cancer_hospital_remarks: Optional[str] = None
    donations_made_to_icddrb: int = 0
    donations_made_to_icddrb_remarks: Optional[str] = None
    donation_given_at_crp_savar: int = 0
    donation_given_at_crp_savar_remarks: Optional[str] = None
    donations_to_charitable_or_educational_institutions_approved_by_the_government: int = 0
    donations_to_charitable_or_educational_institutions_approved_by_the_government_remarks: Optional[str] = None
    donation_to_asiatic_society_bangladesh: int = 0
    donation_to_asiatic_society_bangladesh_remarks: Optional[str] = None
    donation_to_dhaka_ahsania_mission_cancer_hospital: int = 0
    donation_to_dhaka_ahsania_mission_cancer_hospital_remarks: Optional[str] = None
    contribution_paid_to_super_annuity_fund: int = 0
    contribution_paid_to_super_annuity_fund_remarks: Optional[str] = None
    other: int = 0
    other_remarks: Optional[str] = None
    total : int =0
    allowable_investment : int = 0

    @property
    def total(self):
        return (
            self.gov_securities +
            self.eft +
            self.life_insurance_policy_value +
            self.life_insurance_given_premium +
            self.premium_or_contractual_deferred_annuity_of_life_insurance_policy_paid_in_Bangladesh +
            self.contribution_paid_to_deposit_pension_or_monthly_savings_scheme +
            self.investment_in_any_securities_listed_with_an_authorized_stock_exchange +
            self.provisions_of_pf_Act_1925_apply_to_the_contribution_of_the_taxpayer_to_any_such_fund +
            self.contributions_made_by_the_taxpayer_and_his_employer_to_an_approved_provident_fund +
            self.contributions_paid_to_approved_superannuation_funds +
            self.contribution_paid_to_welfare_fund_group_insurance_fund +
            self.contribution_paid_to_zakat_fund +
            self.donation_to_any_national_level_institution_dedicated_to_the_preservation_of_the_memory_of_the_liberation_war +
            self.donations_to_national_institutions_to_preserve_the_memory_of_the_father_of_the_nation +
            self.donation_to_organizations_established_for_the_welfare_of_the_disabled +
            self.donations_made_to_the_liberation_war_museum +
            self.donation_to_ahsania_cancer_hospital +
            self.donations_made_to_icddrb +
            self.donation_given_at_crp_savar +
            self.donations_to_charitable_or_educational_institutions_approved_by_the_government +
            self.donation_to_asiatic_society_bangladesh +
            self.donation_to_dhaka_ahsania_mission_cancer_hospital +
            self.contribution_paid_to_super_annuity_fund +
            self.other
        )

    class Config:
        orm_mode = True
        
        
class Rebate_Record(BaseModel):
    etin : str
    actual_investment : int = 0
    allowable_investment : int = 0
    rebate : int = 0
    
    class config:
        orm_mode = True
        
        
        

        