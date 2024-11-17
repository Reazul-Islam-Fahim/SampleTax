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


    
def create_tax_payer(db: Session, tax_payer: schemas.TaxPayerCreate):
    db_tax_payer = models.Taxpayer(
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
        etin=salary.etin
    )

    db.add(salary_income_record)
    db.commit()
    db.refresh(salary_income_record)
    return salary_income_record






def get_salary_income_summary(db: Session, etin: str):
    return db.query(models.SalaryIncomeSummary).filter(models.SalaryIncomeSummary.etin == etin).first()

def get_salary_income_summarys(db: Session, skip: int , limit: int):
    return db.query(models.SalaryIncomeSummary).offset(skip).limit(limit).all()


def create_salary_income_summary(db: Session, salary_summary: schemas.SalaryIncome_Summary):
    salary_income_summary = models.SalaryIncomeSummary(
        etin = salary_summary.etin,
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


def create_investment_record(db: Session, investment_record: schemas.Investment_Record):
    investment_record = models.InvestmentRecord(
        etin = investment_record.etin,
        gov_securities=investment_record.gov_securities,
        eft=investment_record.eft,
        life_insurance_policy_value=investment_record.life_insurance_policy_value,
        life_insurance_given_premium=investment_record.life_insurance_given_premium,
        other=investment_record.other
    )
    
    db.add(investment_record)
    db.commit()
    db.refresh(investment_record)
    return investment_record




def get_rebate_record(db: Session, etin: str):
    return db.query(models.RebateRecord).filter(models.RebateRecord.etin == etin).first()

def get_rebate_records(db: Session, skip: int , limit: int):
    return db.query(models.RebateRecord).offset(skip).limit(limit).all()


def create_rebate_record(db: Session, rebate_record: schemas.Rebate_Record):
    rebate_record = models.InvestmentRecord(
        etin = rebate_record.etin,
        actual_investment=rebate_record.actual_investment,
        allowable_investment=rebate_record.allowable_investment,
        rebate=rebate_record.rebate
    )
    
    db.add(rebate_record)
    db.commit()
    db.refresh(rebate_record)
    return rebate_record



