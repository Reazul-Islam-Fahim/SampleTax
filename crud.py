from sqlalchemy.orm import Session
import models, schemas


def get_user_auth(db: Session, id: int):
    return db.query(models.UserAuth).filter(models.UserAuth.id == id).first()

def get_user_auths(db: Session, skip: int , limit: int):
    return db.query(models.UserAuth).offset(skip).limit(limit).all()


    
def create_user_auth(db: Session, user_auth: schemas.User_Auth):
    db_user_auth = models.UserAuth(
        username=user_auth.username,
        email=user_auth.email,
        password=user_auth.password,
    )
    
    db.add(db_user_auth)
    db.commit()
    db.refresh(db_user_auth)
    return db_user_auth




def get_tax_payer(db: Session, etin: str):
    return db.query(models.Taxpayer).filter(models.Taxpayer.etin == etin).first()

def get_tax_payers(db: Session, skip: int , limit: int):
    return db.query(models.Taxpayer).offset(skip).limit(limit).all()


    
def create_tax_payer(db: Session, tax_payer: schemas.TaxPayerCreate, user_id : int):
    db_tax_payer = models.Taxpayer(
        user_id=user_id,
        etin=tax_payer.etin,
        nid=tax_payer.nid,
        name=tax_payer.name,
        gender=tax_payer.gender,
        circle=tax_payer.circle,
        zone=tax_payer.zone,
        employment_type=tax_payer.employment_type,
        company_name=tax_payer.company_name,
        assesment_year=tax_payer.assesment_year,
        residential_status=tax_payer.residential_status,
        freedom_fighter=tax_payer.freedom_fighter,
        disable=tax_payer.disable,
        parent_of_disable=tax_payer.parent_of_disable,
        num_autistic_children=tax_payer.num_autistic_children,
        age_above_65=tax_payer.age_above_65,
        date_of_birth=tax_payer.date_of_birth,
        spouse_name=tax_payer.spouse_name,
        spouse_tin=tax_payer.spouse_tin,
        address=tax_payer.address,
        telephone=tax_payer.telephone,
        mobile=tax_payer.mobile,
        email=tax_payer.email,
        employer_name=tax_payer.employer_name,
        name_of_organization=tax_payer.name_of_organization,
        bin_no=tax_payer.bin_no,
        name_tin_partners=tax_payer.name_tin_partners,
    )
    
    db.add(db_tax_payer)
    db.commit()
    db.refresh(db_tax_payer)
    return db_tax_payer






def get_employer_info(db: Session, etin: str):
    return db.query(models.EmployerInfo).filter(models.EmployerInfo.etin == etin).first()

def get_employer_infos(db: Session, skip: int , limit: int):
    return db.query(models.EmployerInfo).offset(skip).limit(limit).all()


    
def create_employer_info(db: Session, employer_info: schemas.Employer_info, petin : str ):
    db_employer_info = models.EmployerInfo(
        etin=petin,
        name=employer_info.name,
        start_date=employer_info.start_date,
        end_date=employer_info.end_date,
    )
    
    db.add(db_employer_info)
    db.commit()
    db.refresh(db_employer_info)
    return db_employer_info





def get_salary_income_record(db: Session, etin: str):
    return db.query(models.SalaryIncomeRecord).filter(models.SalaryIncomeRecord.etin == etin).first()

def get_salary_income_records(db: Session, skip: int , limit: int):
    return db.query(models.SalaryIncomeRecord).offset(skip).limit(limit).all()


def create_salary_income_record(db: Session, salary: schemas.SalaryIncome_Record):
    """
    Create a salary income record using data from a schema instance.

    :param db: SQLAlchemy session
    :param salary: Schema instance containing salary income record data
    :return: Created SalaryIncomeRecord instance
    """
    salary_income_record = models.SalaryIncomeRecord(
        basic_salary=salary.basic_salary,
        basic_salary_remarks=salary.basic_salary_remarks,
        private_allowances=salary.private_allowances,
        private_allowances_remarks=salary.private_allowances_remarks,
        private_arrear_salary=salary.private_arrear_salary,
        private_arrear_salary_remarks=salary.private_arrear_salary_remarks,
        private_gratuity=salary.private_gratuity,
        private_gratuity_remarks=salary.private_gratuity_remarks,
        private_perquisites=salary.private_perquisites,
        private_perquisites_remarks=salary.private_perquisites_remarks,
        private_receipts_or_additional_receipts_in_lieu_of_salary=salary.private_receipts_or_additional_receipts_in_lieu_of_salary,
        private_receipts_or_additional_receipts_in_lieu_of_salary_remarks=salary.private_receipts_or_additional_receipts_in_lieu_of_salary_remarks,
        private_income_from_employee_share_scheme=salary.private_income_from_employee_share_scheme,
        private_income_from_employee_share_scheme_remarks=salary.private_income_from_employee_share_scheme_remarks,
        private_housing_facility=salary.private_housing_facility,
        private_housing_facility_remarks=salary.private_housing_facility_remarks,
        private_vehicle_facility=salary.private_vehicle_facility,
        private_vehicle_facility_remarks=salary.private_vehicle_facility_remarks,
        private_any_other_benefit_provided_by_the_employer=salary.private_any_other_benefit_provided_by_the_employer,
        private_any_other_benefit_provided_by_the_employer_remarks=salary.private_any_other_benefit_provided_by_the_employer_remarks,
        private_contribution_paid_by_employer_to_recognized_pf=salary.private_contribution_paid_by_employer_to_recognized_pf,
        private_contribution_paid_by_employer_to_recognized_pf_remarks=salary.private_contribution_paid_by_employer_to_recognized_pf_remarks,
        private_others=salary.private_others,
        private_others_remarks=salary.private_others_remarks,
        
        
        
        gov_arrear_pay=salary.gov_arrear_pay,
        gov_arrear_pay_remarks=salary.gov_arrear_pay_remarks,
        gov_festival_allowance=salary.gov_festival_allowance,
        gov_festival_allowance_remarks=salary.gov_festival_allowance_remarks,
        gov_special_allowance=salary.gov_special_allowance,
        gov_special_allowance_remarks=salary.gov_special_allowance_remarks,
        gov_support_staff_allowance=salary.gov_support_staff_allowance,
        gov_support_staff_allowance_remarks=salary.gov_support_staff_allowance_remarks,
        gov_leave_allowance=salary.gov_leave_allowance,
        gov_leave_allowance_remarks=salary.gov_leave_allowance_remarks,
        gov_reward=salary.gov_reward,
        gov_reward_remarks=salary.gov_reward_remarks,
        gov_overtime=salary.gov_overtime,
        gov_overtime_remarks=salary.gov_overtime_remarks,
        gov_bangla_noboborsho=salary.gov_bangla_noboborsho,
        gov_bangla_noboborsho_remarks=salary.gov_bangla_noboborsho_remarks,
        gov_interest_accrued_from_PF=salary.gov_interest_accrued_from_PF,
        gov_interest_accrued_from_PF_remarks=salary.gov_interest_accrued_from_PF_remarks,
        gov_lump_grant=salary.gov_lump_grant,
        gov_lump_grant_remarks=salary.gov_lump_grant_remarks,
        gov_gratuity=salary.gov_gratuity,
        gov_gratuity_remarks=salary.gov_gratuity_remarks,
        gov_others=salary.gov_others,
        gov_others_remarks=salary.gov_others_remarks,
        etin=salary.etin,
        employer_info_id=salary.employer_info_id
    )

    db.add(salary_income_record)
    db.commit()
    db.refresh(salary_income_record)
    return salary_income_record



def get_allowance(db: Session, etin: str):
    return db.query(models.AllowanceDetails).filter(models.AllowanceDetails.etin == etin).first()

def get_allowances(db: Session, skip: int , limit: int):
    return db.query(models.AllowanceDetails).offset(skip).limit(limit).all()


def create_allowance(db: Session, allowances: schemas.Allowance_Details, petin : str ):
    allowances = models.AllowanceDetails(
        etin = petin,
        any_allowance = allowances.any_allowance,
        any_allowance_remarks = allowances.any_allowance_remarks,
        leave_allowance = allowances.leave_allowance,
        leave_allowance_remarks = allowances.leave_allowance_remarks,
        lump_grant = allowances.lump_grant,
        lump_grant_remarks = allowances.lump_grant_remarks,
        bonus = allowances.bonus,
        bonus_remarks = allowances.bonus_remarks,
        fee = allowances.fee,
        fee_remarks = allowances.fee_remarks,
        commission = allowances.commission,
        commission_remarks = allowances.commission_remarks,
        overtime = allowances.overtime,
        overtime_remarks = allowances.overtime_remarks,
        other = allowances.other,
        other_details = allowances.other_details,
        total = allowances.total
    )
    
    db.add(allowances)
    db.commit()
    db.refresh(allowances)
    return allowances




def get_perquisite(db: Session, etin: str):
    return db.query(models.PerquisiteDetails).filter(models.PerquisiteDetails.etin == etin).first()

def get_perquisites(db: Session, skip: int , limit: int):
    return db.query(models.PerquisiteDetails).offset(skip).limit(limit).all()


def create_perquisite(db: Session, perquisite: schemas.Perquisite_Details, petin : str ):
    perquisite = models.PerquisiteDetails(
        etin = petin,
        # salary_income_record_id = perquisite.salary_income_record_id,
        mohargha_allowance = perquisite.mohargha_allowance,
        mohargha_allowance_remarks = perquisite.mohargha_allowance_remarks,
        insurance_premium_borne_by_the_employer = perquisite.insurance_premium_borne_by_the_employer,
        insurance_premium_borne_by_the_employer_remarks = perquisite.insurance_premium_borne_by_the_employer_remarks,
        housing_allowance = perquisite.housing_allowance,
        housing_allowance_remarks = perquisite.housing_allowance_remarks,
        house_rent_allowance = perquisite.house_rent_allowance,
        house_rent_allowance_remarks = perquisite.house_rent_allowance_remarks,
        entertainment_allowance = perquisite.entertainment_allowance,
        entertainment_allowance_remarks = perquisite.entertainment_allowance_remarks,
        passage_leave = perquisite.passage_leave,
        passage_leave_remarks = perquisite.passage_leave_remarks,
        medical_allowance = perquisite.medical_allowance,
        medical_allowance_remarks = perquisite.medical_allowance_remarks,
        any_other_obligations_of_the_employee = perquisite.any_other_obligations_of_the_employee,
        any_other_obligations_of_the_employee_remarks = perquisite.any_other_obligations_of_the_employee_remarks,
        other = perquisite.other,
        other_remarks = perquisite.other_remarks,
        total = perquisite.total

    )
    
    db.add(perquisite)
    db.commit()
    db.refresh(perquisite)
    return perquisite



def get_vehicle_falitiy(db: Session, etin: str):
    return db.query(models.VehicleFacilityDetails).filter(models.VehicleFacilityDetails.etin == etin).first()

def get_vehicle_falities(db: Session, skip: int , limit: int):
    return db.query(models.VehicleFacilityDetails).offset(skip).limit(limit).all()


def create_vehicle_falitiy(db: Session, vehicle_facility: schemas.Vehicale_facility_Details, petin : str ):
    vehicle_facility = models.VehicleFacilityDetails(
        etin = petin,
        # salary_income_record_id = vehicle_facility.salary_income_record_id,
        upto_2500CC = vehicle_facility.upto_2500CC,
        cost_for_upto_2500 = vehicle_facility.cost_for_upto_2500,
        greater_than_2500cc = vehicle_facility.greater_than_2500cc,
        cost_for_more_than_2500 = vehicle_facility.cost_for_more_than_2500,
        no_of_months = vehicle_facility.no_of_months,
        total = vehicle_facility.total
    )
    
    db.add(vehicle_facility)
    db.commit()
    db.refresh(vehicle_facility)
    return vehicle_facility






def get_salary_income_summary(db: Session, etin: str):
    return db.query(models.SalaryIncomeSummary).filter(models.SalaryIncomeSummary.etin == etin).first()

def get_salary_income_summarys(db: Session, skip: int , limit: int):
    return db.query(models.SalaryIncomeSummary).offset(skip).limit(limit).all()


def create_salary_income_summary(db: Session, salary_summary: schemas.SalaryIncome_Summary, petin : str ):
    salary_income_summary = models.SalaryIncomeSummary(
        etin = petin,
        total_income=salary_summary.total_income,
        exempted_income=salary_summary.exempted_income,
        taxable_income=salary_summary.taxable_income,
        tax_liability=salary_summary.tax_liability
        
    )
    
    db.add(salary_income_summary)
    db.commit()
    db.refresh(salary_income_summary)
    return salary_income_summary




def get_investment_record(db: Session, etin: str):
    return db.query(models.InvestmentRecord).filter(models.InvestmentRecord.etin == etin).first()

def get_investment_records(db: Session, skip: int , limit: int):
    return db.query(models.InvestmentRecord).offset(skip).limit(limit).all()


def create_investment_record(db: Session, investment_record: schemas.Investment_Record, petin : str):
    investment_record = models.InvestmentRecord(
        etin=petin,
        gov_securities_actual=investment_record.gov_securities_actual,
        gov_securities_allowable=investment_record.gov_securities_allowable,
        gov_securities_remarks=investment_record.gov_securities_remarks,
        
        eft_actual=investment_record.eft_actual,
        eft_allowable=investment_record.eft_allowable,
        eft_remarks=investment_record.eft_remarks,
        
        life_insurance_given_premium_actual=investment_record.life_insurance_given_premium_actual,
        life_insurance_given_premium_allowable=investment_record.life_insurance_given_premium_allowable,
        life_insurance_given_premium_remarks=investment_record.life_insurance_given_premium_remarks,
        
         
        contribution_paid_to_deposit_pension_actual=investment_record.contribution_paid_to_deposit_pension_actual,
        contribution_paid_to_deposit_pension_allowable=investment_record.contribution_paid_to_deposit_pension_allowable,
        contribution_paid_to_deposit_pension_remarks=investment_record.contribution_paid_to_deposit_pension_remarks,
        
        premium_or_contractual_deferred_annuity_actual=investment_record.premium_or_contractual_deferred_annuity_actual,
        premium_or_contractual_deferred_annuity_allowable=investment_record.premium_or_contractual_deferred_annuity_actual,
        premium_or_contractual_deferred_annuity_remarks=investment_record.premium_or_contractual_deferred_annuity_remarks,
       
        investment_in_any_securities_actual=investment_record.investment_in_any_securities_actual,
        investment_in_any_securities_allowable=investment_record.investment_in_any_securities_actual,
        investment_in_any_securities_remarks=investment_record.investment_in_any_securities_remarks,
        
        provisions_of_pf_act_1925_actual=investment_record.provisions_of_pf_act_1925_actual,
        provisions_of_pf_act_1925_allowable=investment_record.provisions_of_pf_act_1925_actual,
        provisions_of_pf_act_1925_remarks=investment_record.provisions_of_pf_act_1925_remarks,
        
        contributions_to_approved_provident_fund_actual=investment_record.contributions_to_approved_provident_fund_actual,
        contributions_to_approved_provident_fund_allowable=investment_record.contributions_to_approved_provident_fund_actual,
        contributions_to_approved_provident_fund_remarks=investment_record.contributions_to_approved_provident_fund_remarks,
        
        contributions_to_superannuation_funds_actual=investment_record.contributions_to_superannuation_funds_actual,
        contributions_to_superannuation_funds_allowable=investment_record.contributions_to_superannuation_funds_actual,
        contributions_to_superannuation_funds_remarks=investment_record.contributions_to_superannuation_funds_remarks,
        
        contribution_to_welfare_fund_actual=investment_record.contribution_to_welfare_fund_actual,
        contribution_to_welfare_fund_allowable=investment_record.contribution_to_welfare_fund_actual,
        contribution_to_welfare_fund_remarks=investment_record.contribution_to_welfare_fund_remarks,
        
        contribution_to_zakat_fund_actual=investment_record.contribution_to_zakat_fund_actual,
        contribution_to_zakat_fund_allowable=investment_record.contribution_to_zakat_fund_actual,
        contribution_to_zakat_fund_remarks=investment_record.contribution_to_zakat_fund_remarks,
        
        donation_to_liberation_war_memory_actual=investment_record.donation_to_liberation_war_memory_actual,
        donation_to_liberation_war_memory_allowable=investment_record.donation_to_liberation_war_memory_actual,
        donation_to_liberation_war_memory_remarks=investment_record.donation_to_liberation_war_memory_remarks,
        
        donations_to_father_of_nation_memory_actual=investment_record.donations_to_father_of_nation_memory_actual,
        donations_to_father_of_nation_memory_allowable=investment_record.donations_to_father_of_nation_memory_actual,
        donations_to_father_of_nation_memory_remarks=investment_record.donations_to_father_of_nation_memory_remarks,
        
        donation_to_disabled_organizations_actual=investment_record.donation_to_disabled_organizations_actual,
        donation_to_disabled_organizations_allowable=investment_record.donation_to_disabled_organizations_actual,
        donation_to_disabled_organizations_remarks=investment_record.donation_to_disabled_organizations_remarks,
        
        donations_to_liberation_war_museum_actual=investment_record.donations_to_liberation_war_museum_actual,
        donations_to_liberation_war_museum_allowable=investment_record.donations_to_liberation_war_museum_actual,
        donations_to_liberation_war_museum_remarks=investment_record.donations_to_liberation_war_museum_remarks,
        
        donation_to_ahsania_cancer_hospital_actual=investment_record.donation_to_ahsania_cancer_hospital_actual,
        donation_to_ahsania_cancer_hospital_allowable=investment_record.donation_to_ahsania_cancer_hospital_actual,
        donation_to_ahsania_cancer_hospital_remarks=investment_record.donation_to_ahsania_cancer_hospital_remarks,
        
        donations_to_icddrb_actual=investment_record.donations_to_icddrb_actual,
        donations_to_icddrb_allowable=investment_record.donations_to_icddrb_actual,
        donations_to_icddrb_remarks=investment_record.donations_to_icddrb_remarks,
        
        donation_to_crp_savar_actual=investment_record.donation_to_crp_savar_actual,
        donation_to_crp_savar_allowable=investment_record.donation_to_crp_savar_actual,
        donation_to_crp_savar_remarks=investment_record.donation_to_crp_savar_remarks,
        
        donations_to_charitable_educational_institutions_actual=investment_record.donations_to_charitable_educational_institutions_actual,
        donations_to_charitable_educational_institutions_allowable=investment_record.donations_to_charitable_educational_institutions_actual,
        donations_to_charitable_educational_institutions_remarks=investment_record.donations_to_charitable_educational_institutions_remarks,
        
        donation_to_asiatic_society_actual=investment_record.donation_to_asiatic_society_actual,
        donation_to_asiatic_society_allowable=investment_record.donation_to_asiatic_society_actual,
        donation_to_asiatic_society_remarks=investment_record.donation_to_asiatic_society_remarks,
        
        donation_to_dhaka_ahsania_mission_actual=investment_record.donation_to_dhaka_ahsania_mission_actual,
        donation_to_dhaka_ahsania_mission_allowable=investment_record.donation_to_dhaka_ahsania_mission_actual,
        donation_to_dhaka_ahsania_mission_remarks=investment_record.donation_to_dhaka_ahsania_mission_remarks,
        
        contribution_to_super_annuity_fund_actual=investment_record.contribution_to_super_annuity_fund_actual,
        contribution_to_super_annuity_fund_allowable=investment_record.contribution_to_super_annuity_fund_actual,
        contribution_to_super_annuity_fund_remarks=investment_record.contribution_to_super_annuity_fund_remarks,
        
        other_actual=investment_record.other_actual,
        other_allowable=investment_record.other_actual,
        other_remarks=investment_record.other_remarks,
        
        total_investment=investment_record.total_investment,
        allowable_investment=investment_record.allowable_investment
   
    )

    db.add(investment_record)
    db.commit()
    db.refresh(investment_record)
    return investment_record



def get_given_premium(db: Session, etin : str):
    return db.query(models.GivenPremium).filter(models.GivenPremium.etin == etin).first()

def get_given_premiums(db: Session, skip: int , limit: int):
    return db.query(models.GivenPremium).offset(skip).limit(limit).all()


def create_given_premium(db: Session, given_premium: schemas.Given_Premium, petin : str ):
    given_premium = models.GivenPremium(
        etin = petin,
        policy_no=given_premium.policy_no,
        company=given_premium.company,
        policy_value=given_premium.policy_value,
        given_premium=given_premium.given_premium,
        allowable=given_premium.allowable,
        remarks=given_premium.remarks
    )
    
    db.add(given_premium)
    db.commit()
    db.refresh(given_premium)
    return given_premium



def get_gov_securities(db: Session, etin : str):
    return db.query(models.GovSecurities).filter(models.GovSecurities.etin == etin).first()

def get_gov_securitiess(db: Session, skip: int , limit: int):
    return db.query(models.GovSecurities).offset(skip).limit(limit).all()


def create_gov_securities(db: Session, gov_securities: schemas.Gov_Securities, petin : str ):
    gov_securities = models.GovSecurities(
        etin = petin,
        description=gov_securities.description,
        actual=gov_securities.actual,
        allowable=gov_securities.allowable
    )
    
    db.add(gov_securities)
    db.commit()
    db.refresh(gov_securities)
    return gov_securities



def get_eft(db: Session, etin : str):
    return db.query(models.EFT).filter(models.EFT.etin == etin).first()

def get_efts(db: Session, skip: int , limit: int):
    return db.query(models.EFT).offset(skip).limit(limit).all()


def create_eft(db: Session, eft: schemas.E_FT, petin : str ):
    eft = models.EFT(
        etin = petin,
        description=eft.description,
        actual=eft.actual,
        allowable=eft.allowable
    )
    
    db.add(eft)
    db.commit()
    db.refresh(eft)
    return eft



def get_dps(db: Session, etin : str):
    return db.query(models.DPS).filter(models.DPS.etin == etin).first()

def get_dpss(db: Session, skip: int , limit: int):
    return db.query(models.DPS).offset(skip).limit(limit).all()


def create_dps(db: Session, dps: schemas.D_PS, petin : str ):
    dps = models.DPS(
        etin = petin,
        description=dps.description,
        actual=dps.actual,
        allowable=dps.allowable
    )
    
    db.add(dps)
    db.commit()
    db.refresh(dps)
    return dps




def get_rebate_record(db: Session, etin: str):
    return db.query(models.RebateRecord).filter(models.RebateRecord.etin == etin).first()

def get_rebate_records(db: Session, skip: int , limit: int):
    return db.query(models.RebateRecord).offset(skip).limit(limit).all()


def create_rebate_record(db: Session, rebate_record: int, petin : str, taxable_income : int, allowable_investment : int ):
    rebate_record = models.RebateRecord(
        etin = petin,
        taxable_income=taxable_income,
        allowable_investment=allowable_investment,
        rebate=rebate_record
    )
    
    db.add(rebate_record)
    db.commit()
    db.refresh(rebate_record)
    return rebate_record



def get_tax_record(db: Session, etin: str):
    return db.query(models.RebateRecord).filter(models.RebateRecord.etin == etin).first()

def get_tax_records(db: Session, skip: int , limit: int):
    return db.query(models.RebateRecord).offset(skip).limit(limit).all()


def create_tax_record(db: Session, tax_record: schemas.Tax_Record, petin : str):
    tax_record = models.TaxRecord(
        etin = petin,
        net_taxable_income=tax_record.net_taxable_income,
        area_tax=tax_record.area_tax,
        actual_payable_tax=tax_record.actual_payable_tax
    )
    
    db.add(tax_record)
    db.commit()
    db.refresh(tax_record)
    return tax_record





