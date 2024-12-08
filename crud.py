from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException


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



def update_user_auth(db: Session, id: int, updated_user_auth: schemas.User_Auth):

    db_user_auth = db.query(models.UserAuth).filter(models.UserAuth.id == id).first()

    if not db_user_auth:
        return None  # Record does not exist

    db_user_auth.username = updated_user_auth.username,
    db_user_auth.email = updated_user_auth.email,
    db_user_auth.password = updated_user_auth.password, # Ensure password is handled securely in production

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
        tax_payer_status = tax_payer.tax_payer_status,
        freedom_fighter=tax_payer.freedom_fighter,
        disable=tax_payer.disable,
        parent_of_disable=tax_payer.parent_of_disable,
        num_autistic_children=tax_payer.num_autistic_children,
        age_above_65=tax_payer.age_above_65,
        date_of_birth=tax_payer.date_of_birth,
        father_name=tax_payer.father_name,
        marital_status = tax_payer.marital_status,
        spouse_name=tax_payer.spouse_name,
        spouse_tin=tax_payer.spouse_tin,
        permanent_address=tax_payer.permanent_address,
        present_address = tax_payer.present_address,
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


def update_tax_payer(db: Session, etin: str, updated_tax_payer: schemas.TaxPayerCreate):

    db_tax_payer = db.query(models.Taxpayer).filter(models.Taxpayer.etin == etin).first()

    if not db_tax_payer:
        return None 

    db_tax_payer.nid = updated_tax_payer.nid,
    db_tax_payer.name = updated_tax_payer.name,
    db_tax_payer.gender = updated_tax_payer.gender,
    db_tax_payer.circle = updated_tax_payer.circle,
    db_tax_payer.zone = updated_tax_payer.zone,
    db_tax_payer.employment_type = updated_tax_payer.employment_type,
    db_tax_payer.company_name = updated_tax_payer.company_name,
    db_tax_payer.assesment_year = updated_tax_payer.assesment_year,
    db_tax_payer.residential_status = updated_tax_payer.residential_status,
    db_tax_payer.tax_payer_status = updated_tax_payer.tax_payer_status,
    db_tax_payer.freedom_fighter = updated_tax_payer.freedom_fighter,
    db_tax_payer.disable = updated_tax_payer.disable,
    db_tax_payer.parent_of_disable = updated_tax_payer.parent_of_disable,
    db_tax_payer.num_autistic_children = updated_tax_payer.num_autistic_children,
    db_tax_payer.age_above_65 = updated_tax_payer.age_above_65,
    db_tax_payer.date_of_birth = updated_tax_payer.date_of_birth,
    db_tax_payer.father_name = updated_tax_payer.father_name,
    db_tax_payer.marital_status = updated_tax_payer.marital_status,
    db_tax_payer.spouse_name = updated_tax_payer.spouse_name,
    db_tax_payer.spouse_tin = updated_tax_payer.spouse_tin,
    db_tax_payer.permanant_address = updated_tax_payer.permanant_address,
    db_tax_payer.present_address = updated_tax_payer.present_address,
    db_tax_payer.telephone = updated_tax_payer.telephone,
    db_tax_payer.mobile = updated_tax_payer.mobile,
    db_tax_payer.email = updated_tax_payer.email,
    db_tax_payer.employer_name = updated_tax_payer.employer_name,
    db_tax_payer.name_of_organization = updated_tax_payer.name_of_organization,
    db_tax_payer.bin_no = updated_tax_payer.bin_no,
    db_tax_payer.name_tin_partners = updated_tax_payer.name_tin_partners,

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


def update_employer_info(db: Session, etin: str, updated_employer_info: schemas.Employer_info):
    db_employer_info = db.query(models.EmployerInfo).filter(models.EmployerInfo.etin == etin).first()

    if not db_employer_info:
        return None  # Record does not exist

    # Update fields with new data
    db_employer_info.name = updated_employer_info.name,
    db_employer_info.start_date = updated_employer_info.start_date,
    db_employer_info.end_date = updated_employer_info.end_date,

    # Commit changes to the database
    db.commit()
    db.refresh(db_employer_info)

    return db_employer_info






def get_salary_income_record(db: Session, etin: str):
    return db.query(models.SalaryIncomeRecord).filter(models.SalaryIncomeRecord.etin == etin).first()

def get_salary_income_records(db: Session, skip: int , limit: int):
    return db.query(models.SalaryIncomeRecord).offset(skip).limit(limit).all()


def create_salary_income_record(db: Session, salary: schemas.SalaryIncome_Record):
 
    salary_income_record = models.SalaryIncomeRecord(
        basic_salary=salary.basic_salary,
        basic_salary_exempted=0,
        basic_salary_taxable=salary.basic_salary,
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
        gov_arrear_pay_exempted=salary.gov_arrear_pay,
        gov_arrear_pay_taxable=0,
        gov_arrear_pay_remarks=salary.gov_arrear_pay_remarks,
        
        gov_special_allowance=salary.gov_special_allowance,
        gov_special_allowance_exempted=salary.gov_special_allowance_exempted,
        gov_special_allowance_taxable=salary.gov_special_allowance_taxable,
        gov_special_allowance_remarks=salary.gov_special_allowance_remarks,
        
        gov_medical_allowance=salary.gov_medical_allowance,
        gov_medical_allowance_exempted=salary.gov_medical_allowance_exempted,
        gov_medical_allowance_taxable=salary.gov_medical_allowance_taxable,
        gov_medical_allowance_remarks=salary.gov_medical_allowance_remarks,

        gov_conveyance_allowance=salary.gov_conveyance_allowance,
        gov_conveyance_allowance_exempted=salary.gov_conveyance_allowance_exempted,
        gov_conveyance_allowance_taxable=salary.gov_conveyance_allowance_taxable,
        gov_conveyance_allowance_remarks=salary.gov_conveyance_allowance_remarks,

        gov_festival_allowance=salary.gov_festival_allowance,
        gov_festival_allowance_exempted=salary.gov_festival_allowance_exempted,
        gov_festival_allowance_taxable=salary.gov_festival_allowance_taxable,
        gov_festival_allowance_remarks=salary.gov_festival_allowance_remarks,

        gov_house_rent_allowance=salary.gov_house_rent_allowance,
        gov_house_rent_allowance_exempted=salary.gov_house_rent_allowance_exempted,
        gov_house_rent_allowance_taxable=salary.gov_house_rent_allowance_taxable,
        gov_house_rent_allowance_remarks=salary.gov_house_rent_allowance_remarks,
        
        gov_support_staff_allowance=salary.gov_support_staff_allowance,
        gov_support_staff_allowance_exempted=salary.gov_support_staff_allowance,
        gov_support_staff_allowance_taxable=0,
        gov_support_staff_allowance_remarks=salary.gov_support_staff_allowance_remarks,
        
        gov_leave_allowance=salary.gov_leave_allowance,
        gov_leave_allowance_exempted=salary.gov_leave_allowance,
        gov_leave_allowance_taxable=0,
        gov_leave_allowance_remarks=salary.gov_leave_allowance_remarks,
        
        gov_reward=salary.gov_reward,
        gov_reward_exempted=salary.gov_reward,
        gov_reward_taxable=0,
        gov_reward_remarks=salary.gov_reward_remarks,
        
        gov_overtime=salary.gov_overtime,
        gov_overtime_exempted=salary.gov_overtime,
        gov_overtime_taxable=0,
        gov_overtime_remarks=salary.gov_overtime_remarks,
        
        gov_bangla_noboborsho=salary.gov_bangla_noboborsho,
        gov_bangla_noboborsho_exempted=salary.gov_bangla_noboborsho,
        gov_bangla_noboborsho_taxable=0,
        gov_bangla_noboborsho_remarks=salary.gov_bangla_noboborsho_remarks,
        
        gov_interest_accrued_from_PF=salary.gov_interest_accrued_from_PF,
        gov_interest_accrued_from_PF_exempted=salary.gov_interest_accrued_from_PF,
        gov_interest_accrued_from_PF_taxable=0,
        gov_interest_accrued_from_PF_remarks=salary.gov_interest_accrued_from_PF_remarks,
        
        gov_lump_grant=salary.gov_lump_grant,
        gov_lump_grant_exempted=salary.gov_lump_grant,
        gov_lump_grant_taxable=0,
        gov_lump_grant_remarks=salary.gov_lump_grant_remarks,
        
        gov_gratuity=salary.gov_gratuity,
        gov_gratuity_exempted=salary.gov_gratuity,
        gov_gratuity_taxable=0,
        gov_gratuity_remarks=salary.gov_gratuity_remarks,
        
        gov_others=salary.gov_others,
        gov_others_exempted=salary.gov_others,
        gov_others_taxable=0,
        gov_others_remarks=salary.gov_others_remarks,
        
        etin=salary.etin,
        employer_info_id=salary.employer_info_id
    )

    db.add(salary_income_record)
    db.commit()
    db.refresh(salary_income_record)
    return salary_income_record


def update_salary_income_record(db: Session, etin: str, updated_salary: schemas.SalaryIncome_Record):
  
    # Fetch the existing record
    salary_income_record = db.query(models.SalaryIncomeRecord).filter(models.SalaryIncomeRecord.etin == etin).first()

    if not salary_income_record:
        return None  # Record does not exist

    # Update the fields of the existing record with new data
    salary_income_record.basic_salary = updated_salary.basic_salary,
    salary_income_record.basic_salary_exempted=0,
    salary_income_record.basic_salary_taxable=updated_salary.basic_salary,
    salary_income_record.basic_salary_remarks = updated_salary.basic_salary_remarks,
    
    salary_income_record.private_allowances = updated_salary.private_allowances,
    salary_income_record.private_allowances_remarks = updated_salary.private_allowances_remarks,
    salary_income_record.private_arrear_salary = updated_salary.private_arrear_salary,
    salary_income_record.private_arrear_salary_remarks = updated_salary.private_arrear_salary_remarks,
    salary_income_record.private_gratuity = updated_salary.private_gratuity,
    salary_income_record.private_gratuity_remarks = updated_salary.private_gratuity_remarks,
    salary_income_record.private_perquisites = updated_salary.private_perquisites,
    salary_income_record.private_perquisites_remarks = updated_salary.private_perquisites_remarks,
    salary_income_record.private_receipts_or_additional_receipts_in_lieu_of_salary = updated_salary.private_receipts_or_additional_receipts_in_lieu_of_salary,
    salary_income_record.private_receipts_or_additional_receipts_in_lieu_of_salary_remarks = updated_salary.private_receipts_or_additional_receipts_in_lieu_of_salary_remarks,
    salary_income_record.private_income_from_employee_share_scheme = updated_salary.private_income_from_employee_share_scheme,
    salary_income_record.private_income_from_employee_share_scheme_remarks = updated_salary.private_income_from_employee_share_scheme_remarks,
    salary_income_record.private_housing_facility = updated_salary.private_housing_facility,
    salary_income_record.private_housing_facility_remarks = updated_salary.private_housing_facility_remarks,
    salary_income_record.private_vehicle_facility = updated_salary.private_vehicle_facility,
    salary_income_record.private_vehicle_facility_remarks = updated_salary.private_vehicle_facility_remarks,
    salary_income_record.private_any_other_benefit_provided_by_the_employer = updated_salary.private_any_other_benefit_provided_by_the_employer,
    salary_income_record.private_any_other_benefit_provided_by_the_employer_remarks = updated_salary.private_any_other_benefit_provided_by_the_employer_remarks,
    salary_income_record.private_contribution_paid_by_employer_to_recognized_pf = updated_salary.private_contribution_paid_by_employer_to_recognized_pf,
    salary_income_record.private_contribution_paid_by_employer_to_recognized_pf_remarks = updated_salary.private_contribution_paid_by_employer_to_recognized_pf_remarks,
    salary_income_record.private_others = updated_salary.private_others,
    salary_income_record.private_others_remarks = updated_salary.private_others_remarks,

    salary_income_record.gov_arrear_pay = updated_salary.gov_arrear_pay,
    salary_income_record.gov_arrear_pay_exempted = updated_salary.gov_arrear_pay,
    salary_income_record.gov_arrear_pay_taxable = 0,
    salary_income_record.gov_arrear_pay_remarks = updated_salary.gov_arrear_pay_remarks,
    
    salary_income_record.gov_special_allowance = updated_salary.gov_special_allowance,
    salary_income_record.gov_special_allowance_exempted = updated_salary.gov_special_allowance,
    salary_income_record.gov_special_allowance_taxable = 0,
    salary_income_record.gov_special_allowance_remarks = updated_salary.gov_special_allowance_remarks,

    salary_income_record.gov_medical_allowance = updated_salary.gov_medical_allowance,
    salary_income_record.gov_medical_allowance_exempted = updated_salary.gov_medical_allowance,
    salary_income_record.gov_medical_allowance_taxable = 0,
    salary_income_record.gov_medical_allowance_remarks = updated_salary.gov_medical_allowance_remarks,

    salary_income_record.gov_conveyance_allowance = updated_salary.gov_conveyance_allowance,
    salary_income_record.gov_conveyance_allowance_exempted = updated_salary.gov_conveyance_allowance,
    salary_income_record.gov_conveyance_allowance_taxable = 0,
    salary_income_record.gov_conveyance_allowance_remarks = updated_salary.gov_conveyance_allowance_remarks,
    
    salary_income_record.gov_festival_allowance = updated_salary.gov_festival_allowance,
    salary_income_record.gov_festival_allowance_exempted = 0,
    salary_income_record.gov_festival_allowance_taxable = updated_salary.gov_festival_allowance,
    salary_income_record.gov_festival_allowance_remarks = updated_salary.gov_festival_allowance_remarks,

    salary_income_record.gov_house_rent_allowance = updated_salary.gov_house_rent_allowance,
    salary_income_record.gov_house_rent_allowance_exempted = updated_salary.gov_house_rent_allowance_exempted,
    salary_income_record.gov_house_rent_allowance_taxable = 0,
    salary_income_record.gov_house_rent_allowance_remarks = updated_salary.gov_house_rent_allowance_remarks,

    salary_income_record.gov_support_staff_allowance = updated_salary.gov_support_staff_allowance,
    salary_income_record.gov_support_staff_allowance_exempted = updated_salary.gov_support_staff_allowance,
    salary_income_record.gov_support_staff_allowance_taxable = 0,
    salary_income_record.gov_support_staff_allowance_remarks = updated_salary.gov_support_staff_allowance_remarks,
    
    salary_income_record.gov_leave_allowance = updated_salary.gov_leave_allowance,
    salary_income_record.gov_leave_allowance_exempted = updated_salary.gov_leave_allowance,
    salary_income_record.gov_leave_allowance_taxable = 0,
    salary_income_record.gov_leave_allowance_remarks = updated_salary.gov_leave_allowance_remarks,
    
    salary_income_record.gov_reward = updated_salary.gov_reward,
    salary_income_record.gov_reward_exempted = updated_salary.gov_reward,
    salary_income_record.gov_reward_taxable = 0,
    salary_income_record.gov_reward_remarks = updated_salary.gov_reward_remarks,
    
    salary_income_record.gov_overtime = updated_salary.gov_overtime,
    salary_income_record.gov_overtime_exempted = updated_salary.gov_overtime,
    salary_income_record.gov_overtime_taxable = 0,
    salary_income_record.gov_overtime_remarks = updated_salary.gov_overtime_remarks,
    
    salary_income_record.gov_bangla_noboborsho = updated_salary.gov_bangla_noboborsho,
    salary_income_record.gov_bangla_noboborsho_exempted = updated_salary.gov_bangla_noboborsho,
    salary_income_record.gov_bangla_noboborsho_taxable = 0,
    salary_income_record.gov_bangla_noboborsho_remarks = updated_salary.gov_bangla_noboborsho_remarks,
    
    salary_income_record.gov_interest_accrued_from_PF = updated_salary.gov_interest_accrued_from_PF,
    salary_income_record.gov_interest_accrued_from_PF_exempted = updated_salary.gov_interest_accrued_from_PF,
    salary_income_record.gov_interest_accrued_from_PF_taxable = 0,
    salary_income_record.gov_interest_accrued_from_PF_remarks = updated_salary.gov_interest_accrued_from_PF_remarks,
    
    salary_income_record.gov_lump_grant = updated_salary.gov_lump_grant,
    salary_income_record.gov_lump_grant_exempted = updated_salary.gov_lump_grant,
    salary_income_record.gov_lump_grant_taxable = 0,
    salary_income_record.gov_lump_grant_remarks = updated_salary.gov_lump_grant_remarks,
    
    salary_income_record.gov_gratuity = updated_salary.gov_gratuity,
    salary_income_record.gov_gratuity_exempted = updated_salary.gov_gratuity,
    salary_income_record.gov_gratuity_taxable = 0,
    salary_income_record.gov_gratuity_remarks = updated_salary.gov_gratuity_remarks,
    
    salary_income_record.gov_others = updated_salary.gov_others,
    salary_income_record.gov_others_exempted = updated_salary.gov_others,
    salary_income_record.gov_others_taxable = 0,
    salary_income_record.gov_others_remarks = updated_salary.gov_others_remarks,


    salary_income_record.etin = updated_salary.etin,
    salary_income_record.employer_info_id = updated_salary.employer_info_id,


    # Commit changes to the database
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


def update_allowance(db: Session, etin: str, allowances: schemas.Allowance_Details):
    # Find the existing record by ETIN
    existing_record = db.query(models.AllowanceDetails).filter(models.AllowanceDetails.etin == etin).first()
    
    if not existing_record:
        # If the record doesn't exist, return None or raise an exception
        raise HTTPException(status_code=404, detail="Allowance record not found")
    
    # Update the fields with the new data
    existing_record.any_allowance = allowances.any_allowance,
    existing_record.any_allowance_remarks = allowances.any_allowance_remarks,
    existing_record.leave_allowance = allowances.leave_allowance,
    existing_record.leave_allowance_remarks = allowances.leave_allowance_remarks,
    existing_record.lump_grant = allowances.lump_grant,
    existing_record.lump_grant_remarks = allowances.lump_grant_remarks,
    existing_record.bonus = allowances.bonus,
    existing_record.bonus_remarks = allowances.bonus_remarks,
    existing_record.fee = allowances.fee,
    existing_record.fee_remarks = allowances.fee_remarks,
    existing_record.commission = allowances.commission,
    existing_record.commission_remarks = allowances.commission_remarks,
    existing_record.overtime = allowances.overtime,
    existing_record.overtime_remarks = allowances.overtime_remarks,
    existing_record.other = allowances.other,
    existing_record.other_details = allowances.other_details,
    existing_record.total = allowances.total,

    # Commit the changes to the database
    db.commit()
    db.refresh(existing_record)  # Refresh the instance with the updated data
    
    return existing_record





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


def update_perquisite(db: Session, etin: str, perquisite: schemas.Perquisite_Details):
    # Fetch the existing record by ETIN
    existing_record = db.query(models.PerquisiteDetails).filter(models.PerquisiteDetails.etin == etin).first()
    
    if not existing_record:
        # If the record doesn't exist, return None or raise an exception
        raise HTTPException(status_code=404, detail="Perquisite record not found")
    
    # Update the fields with the new data
    existing_record.mohargha_allowance = perquisite.mohargha_allowance,
    existing_record.mohargha_allowance_remarks = perquisite.mohargha_allowance_remarks,
    existing_record.insurance_premium_borne_by_the_employer = perquisite.insurance_premium_borne_by_the_employer,
    existing_record.insurance_premium_borne_by_the_employer_remarks = perquisite.insurance_premium_borne_by_the_employer_remarks,
    existing_record.housing_allowance = perquisite.housing_allowance,
    existing_record.housing_allowance_remarks = perquisite.housing_allowance_remarks,
    existing_record.house_rent_allowance = perquisite.house_rent_allowance,
    existing_record.house_rent_allowance_remarks = perquisite.house_rent_allowance_remarks,
    existing_record.entertainment_allowance = perquisite.entertainment_allowance,
    existing_record.entertainment_allowance_remarks = perquisite.entertainment_allowance_remarks,
    existing_record.passage_leave = perquisite.passage_leave,
    existing_record.passage_leave_remarks = perquisite.passage_leave_remarks,
    existing_record.medical_allowance = perquisite.medical_allowance,
    existing_record.medical_allowance_remarks = perquisite.medical_allowance_remarks,
    existing_record.any_other_obligations_of_the_employee = perquisite.any_other_obligations_of_the_employee,
    existing_record.any_other_obligations_of_the_employee_remarks = perquisite.any_other_obligations_of_the_employee_remarks,
    existing_record.other = perquisite.other,
    existing_record.other_remarks = perquisite.other_remarks,
    existing_record.total = perquisite.total,

    # Commit the changes to the database
    db.commit()
    db.refresh(existing_record)  # Refresh the instance with updated data
    
    return existing_record




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


def update_vehicle_facility(db: Session, etin: str, vehicle_facility: schemas.Vehicale_facility_Details):
    # Find the existing record by ETIN
    existing_record = db.query(models.VehicleFacilityDetails).filter(models.VehicleFacilityDetails.etin == etin).first()
    
    if not existing_record:
        # If the record doesn't exist, return None or raise an exception
        raise HTTPException(status_code=404, detail="Vehicle facility record not found")
    
    # Update the fields with the new data
    existing_record.upto_2500CC = vehicle_facility.upto_2500CC,
    existing_record.cost_for_upto_2500 = vehicle_facility.cost_for_upto_2500,
    existing_record.greater_than_2500cc = vehicle_facility.greater_than_2500cc,
    existing_record.cost_for_more_than_2500 = vehicle_facility.cost_for_more_than_2500,
    existing_record.no_of_months = vehicle_facility.no_of_months,
    existing_record.total = vehicle_facility.total,

    # Commit the changes to the database
    db.commit()
    db.refresh(existing_record)  # Refresh the instance with updated data
    
    return existing_record






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


def update_salary_income_summary(
    db: Session, etin: str, updated_summary: schemas.SalaryIncome_Summary
):
    db_salary_summary = db.query(models.SalaryIncomeSummary).filter(models.SalaryIncomeSummary.etin == etin).first()

    if not db_salary_summary:
        return None  
    
    db_salary_summary.total_income = updated_summary.total_income,
    db_salary_summary.exempted_income = updated_summary.exempted_income,
    db_salary_summary.taxable_income = updated_summary.taxable_income,
    db_salary_summary.tax_liability = updated_summary.tax_liability,

    # Commit changes to the database
    db.commit()
    db.refresh(db_salary_summary)

    return db_salary_summary





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


def update_investment_record(
    db: Session, etin: str, updated_record: schemas.Investment_Record
):

    db_investment_record = db.query(models.InvestmentRecord).filter(models.InvestmentRecord.etin == etin).first()

    if not db_investment_record:
        return None  # Record does not exist

    # Update the fields with new data
    db_investment_record.gov_securities_actual = updated_record.gov_securities_actual,
    db_investment_record.gov_securities_allowable = updated_record.gov_securities_allowable,
    db_investment_record.gov_securities_remarks = updated_record.gov_securities_remarks,

    db_investment_record.eft_actual = updated_record.eft_actual,
    db_investment_record.eft_allowable = updated_record.eft_allowable,
    db_investment_record.eft_remarks = updated_record.eft_remarks,
    
    db_investment_record.life_insurance_given_premium_actual = updated_record.life_insurance_given_premium_actual,
    db_investment_record.life_insurance_given_premium_allowable = updated_record.life_insurance_given_premium_allowable,
    db_investment_record.life_insurance_given_premium_remarks = updated_record.life_insurance_given_premium_remarks,

    db_investment_record.contribution_paid_to_deposit_pension_actual = updated_record.contribution_paid_to_deposit_pension_actual,
    db_investment_record.contribution_paid_to_deposit_pension_allowable = updated_record.contribution_paid_to_deposit_pension_allowable,
    db_investment_record.contribution_paid_to_deposit_pension_remarks = updated_record.contribution_paid_to_deposit_pension_remarks,

    db_investment_record.investment_in_any_securities_actual = updated_record.investment_in_any_securities_actual,
    db_investment_record.investment_in_any_securities_allowable = updated_record.investment_in_any_securities_actual,
    db_investment_record.investment_in_any_securities_remarks = updated_record.investment_in_any_securities_remarks,

    db_investment_record.provisions_of_pf_act_1925_actual = updated_record.provisions_of_pf_act_1925_actual,
    db_investment_record.provisions_of_pf_act_1925_allowable = updated_record.provisions_of_pf_act_1925_actual,
    db_investment_record.provisions_of_pf_act_1925_remarks = updated_record.provisions_of_pf_act_1925_remarks,

    db_investment_record.contributions_to_approved_provident_fund_actual = updated_record.contributions_to_approved_provident_fund_actual,
    db_investment_record.contributions_to_approved_provident_fund_allowable = updated_record.contributions_to_approved_provident_fund_actual,
    db_investment_record.contributions_to_approved_provident_fund_remarks = updated_record.contributions_to_approved_provident_fund_remarks,

    db_investment_record.contributions_to_superannuation_funds_actual = updated_record.contributions_to_superannuation_funds_actual,
    db_investment_record.contributions_to_superannuation_funds_allowable = updated_record.contributions_to_superannuation_funds_actual,
    db_investment_record.contributions_to_superannuation_funds_remarks = updated_record.contributions_to_superannuation_funds_remarks,

    db_investment_record.contribution_to_welfare_fund_actual = updated_record.contribution_to_welfare_fund_actual,
    db_investment_record.contribution_to_welfare_fund_allowable = updated_record.contribution_to_welfare_fund_actual,
    db_investment_record.contribution_to_welfare_fund_remarks = updated_record.contribution_to_welfare_fund_remarks,

    db_investment_record.contribution_to_zakat_fund_actual = updated_record.contribution_to_zakat_fund_actual,
    db_investment_record.contribution_to_zakat_fund_allowable = updated_record.contribution_to_zakat_fund_actual,
    db_investment_record.contribution_to_zakat_fund_remarks = updated_record.contribution_to_zakat_fund_remarks,

    db_investment_record.donation_to_liberation_war_memory_actual = updated_record.donation_to_liberation_war_memory_actual,
    db_investment_record.donation_to_liberation_war_memory_allowable = updated_record.donation_to_liberation_war_memory_actual,
    db_investment_record.donation_to_liberation_war_memory_remarks = updated_record.donation_to_liberation_war_memory_remarks,

    db_investment_record.donations_to_father_of_nation_memory_actual = updated_record.donations_to_father_of_nation_memory_actual,
    db_investment_record.donations_to_father_of_nation_memory_allowable = updated_record.donations_to_father_of_nation_memory_actual,
    db_investment_record.donations_to_father_of_nation_memory_remarks = updated_record.donations_to_father_of_nation_memory_remarks,

    db_investment_record.donation_to_disabled_organizations_actual = updated_record.donation_to_disabled_organizations_actual,
    db_investment_record.donation_to_disabled_organizations_allowable = updated_record.donation_to_disabled_organizations_actual,
    db_investment_record.donation_to_disabled_organizations_remarks = updated_record.donation_to_disabled_organizations_remarks,
    
    db_investment_record.donations_to_liberation_war_museum_actual = updated_record.donations_to_liberation_war_museum_actual,
    db_investment_record.donations_to_liberation_war_museum_allowable = updated_record.donations_to_liberation_war_museum_actual,
    db_investment_record.donations_to_liberation_war_museum_remarks = updated_record.donations_to_liberation_war_museum_remarks,

    db_investment_record.donation_to_ahsania_cancer_hospital_actual = updated_record.donation_to_ahsania_cancer_hospital_actual,
    db_investment_record.donation_to_ahsania_cancer_hospital_allowable = updated_record.donation_to_ahsania_cancer_hospital_actual,
    db_investment_record.donation_to_ahsania_cancer_hospital_remarks = updated_record.donation_to_ahsania_cancer_hospital_remarks,

    db_investment_record.donations_to_icddrb_actual = updated_record.donations_to_icddrb_actual,
    db_investment_record.donations_to_icddrb_allowable = updated_record.donations_to_icddrb_actual,
    db_investment_record.donations_to_icddrb_remarks = updated_record.donations_to_icddrb_remarks,

    db_investment_record.donation_to_crp_savar_actual = updated_record.donation_to_crp_savar_actual,
    db_investment_record.donation_to_crp_savar_allowable = updated_record.donation_to_crp_savar_actual,
    db_investment_record.donation_to_crp_savar_remarks = updated_record.donation_to_crp_savar_remarks,

    db_investment_record.donations_to_charitable_educational_institutions_actual = updated_record.donations_to_charitable_educational_institutions_actual,
    db_investment_record.donations_to_charitable_educational_institutions_allowable = updated_record.donations_to_charitable_educational_institutions_actual,
    db_investment_record.donations_to_charitable_educational_institutions_remarks = updated_record.donations_to_charitable_educational_institutions_remarks,

    db_investment_record.donation_to_asiatic_society_actual = updated_record.donation_to_asiatic_society_actual,
    db_investment_record.donation_to_asiatic_society_allowable = updated_record.donation_to_asiatic_society_actual,
    db_investment_record.donation_to_asiatic_society_remarks = updated_record.donation_to_asiatic_society_remarks,

    db_investment_record.donation_to_dhaka_ahsania_mission_actual = updated_record.donation_to_dhaka_ahsania_mission_actual,
    db_investment_record.donation_to_dhaka_ahsania_mission_allowable = updated_record.donation_to_dhaka_ahsania_mission_actual,
    db_investment_record.donation_to_dhaka_ahsania_mission_remarks = updated_record.donation_to_dhaka_ahsania_mission_remarks,

    db_investment_record.contribution_to_super_annuity_fund_actual = updated_record.contribution_to_super_annuity_fund_actual,
    db_investment_record.contribution_to_super_annuity_fund_allowable = updated_record.contribution_to_super_annuity_fund_actual,
    db_investment_record.contribution_to_super_annuity_fund_remarks = updated_record.contribution_to_super_annuity_fund_remarks,

    db_investment_record.other_actual = updated_record.other_actual,
    db_investment_record.other_allowable = updated_record.other_actual,
    db_investment_record.other_remarks = updated_record.other_remarks,

    db_investment_record.total_investment = updated_record.total_investment = (
            updated_record.gov_securities_actual +
            updated_record.eft_actual +
            updated_record.life_insurance_given_premium_actual +
            updated_record.contribution_paid_to_deposit_pension_actual +
            updated_record.investment_in_any_securities_actual +
            updated_record.provisions_of_pf_act_1925_actual +
            updated_record.contributions_to_approved_provident_fund_actual +
            updated_record.contributions_to_superannuation_funds_actual +
            updated_record.contribution_to_welfare_fund_actual +
            updated_record.contribution_to_zakat_fund_actual +
            updated_record.donation_to_liberation_war_memory_actual +
            updated_record.donations_to_father_of_nation_memory_actual +
            updated_record.donation_to_disabled_organizations_actual +
            updated_record.donations_to_liberation_war_museum_actual +
            updated_record.donation_to_ahsania_cancer_hospital_actual +
            updated_record.donations_to_icddrb_actual +
            updated_record.donation_to_crp_savar_actual +
            updated_record.donations_to_charitable_educational_institutions_actual +
            updated_record.donation_to_asiatic_society_actual +
            updated_record.donation_to_dhaka_ahsania_mission_actual +
            updated_record.contribution_to_super_annuity_fund_actual +
            updated_record.other_actual
        )

 
    
    db_investment_record.allowable_investment = updated_record.allowable_investment = (
            updated_record.gov_securities_allowable +
            updated_record.eft_allowable +
            updated_record.life_insurance_given_premium_allowable +
            updated_record.contribution_paid_to_deposit_pension_allowable +
            updated_record.investment_in_any_securities_allowable +
            updated_record.provisions_of_pf_act_1925_allowable +
            updated_record.contributions_to_approved_provident_fund_allowable +
            updated_record.contributions_to_superannuation_funds_allowable +
            updated_record.contribution_to_welfare_fund_allowable +
            updated_record.contribution_to_zakat_fund_allowable +
            updated_record.donation_to_liberation_war_memory_allowable +
            updated_record.donations_to_father_of_nation_memory_allowable +
            updated_record.donation_to_disabled_organizations_allowable +
            updated_record.donations_to_liberation_war_museum_allowable +
            updated_record.donation_to_ahsania_cancer_hospital_allowable +
            updated_record.donations_to_icddrb_allowable +
            updated_record.donation_to_crp_savar_allowable +
            updated_record.donations_to_charitable_educational_institutions_allowable +
            updated_record.donation_to_asiatic_society_allowable +
            updated_record.donation_to_dhaka_ahsania_mission_allowable +
            updated_record.contribution_to_super_annuity_fund_allowable +
            updated_record.other_allowable
        )

    # Commit changes to the database
    db.commit()
    db.refresh(db_investment_record)

    return db_investment_record




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


def update_given_premium(db: Session, etin: str, given_premium: schemas.Given_Premium):
    # Find the existing record by ETIN
    existing_record = db.query(models.GivenPremium).filter(models.GivenPremium.etin == etin).first()
    
    if not existing_record:
        # If the record doesn't exist, return None or raise an exception
        raise HTTPException(status_code=404, detail="Given premium record not found")
    
    # Update the fields with the new data
    existing_record.policy_no = given_premium.policy_no,
    existing_record.company = given_premium.company,
    existing_record.policy_value = given_premium.policy_value,
    existing_record.given_premium = given_premium.given_premium,
    existing_record.allowable = given_premium.allowable,
    existing_record.remarks = given_premium.remarks,

    # Commit the changes to the database
    db.commit()
    db.refresh(existing_record)  # Refresh the instance with updated data
    
    return existing_record




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


def update_gov_securities(db: Session, etin: str, gov_securities: schemas.Gov_Securities):
    # Find the existing record by ETIN
    existing_record = db.query(models.GovSecurities).filter(models.GovSecurities.etin == etin).first()
    
    if not existing_record:
        # If the record doesn't exist, return None or raise an exception
        raise HTTPException(status_code=404, detail="Gov securities record not found")
    
    # Update the fields with the new data
    existing_record.description = gov_securities.description,
    existing_record.actual = gov_securities.actual,
    existing_record.allowable = gov_securities.allowable,

    # Commit the changes to the database
    db.commit()
    db.refresh(existing_record)  # Refresh the instance with updated data
    
    return existing_record



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


def update_eft(db: Session, etin: str, eft: schemas.E_FT):
    # Find the existing record by ETIN
    existing_record = db.query(models.EFT).filter(models.EFT.etin == etin).first()
    
    if not existing_record:
        # If the record doesn't exist, return None or raise an exception
        raise HTTPException(status_code=404, detail="EFT record not found")
    
    # Update the fields with the new data
    existing_record.description = eft.description,
    existing_record.actual = eft.actual,
    existing_record.allowable = eft.allowable,

    # Commit the changes to the database
    db.commit()
    db.refresh(existing_record)  # Refresh the instance with updated data
    
    return existing_record



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


def update_dps(db: Session, etin: str, dps: schemas.D_PS):
    # Find the existing record by ETIN
    existing_record = db.query(models.DPS).filter(models.DPS.etin == etin).first()
    
    if not existing_record:
        # If the record doesn't exist, raise an HTTP exception
        raise HTTPException(status_code=404, detail="DPS record not found")
    
    # Update the fields with the new data
    existing_record.description = dps.description,
    existing_record.actual = dps.actual,
    existing_record.allowable = dps.allowable,

    # Commit the changes to the database
    db.commit()
    db.refresh(existing_record)  # Refresh the instance with updated data
    
    return existing_record



def get_financial_asset_income(db: Session, etin: str):
    return db.query(models.FinancialAssetIncome).filter(models.FinancialAssetIncome.etin == etin).first()

def get_financial_asset_incomes(db: Session, skip: int , limit: int):
    return db.query(models.FinancialAssetIncome).offset(skip).limit(limit).all()

def create_financial_asset_income(db: Session, financial_asset_income: schemas.Financial_Asset_Income, petin : str ):
    financial_asset_income = models.FinancialAssetIncome(
        etin=petin,
        
        # Savings Bank Interest
        savings_ban_interest_net_income=financial_asset_income.savings_ban_interest_net_income,
        savings_ban_interest_tax_deduction_at_source=financial_asset_income.savings_ban_interest_tax_deduction_at_source,
        savings_ban_interest_interest_on_loans=financial_asset_income.savings_ban_interest_interest_on_loans,
        savings_ban_interest_allowable_expenditure=financial_asset_income.savings_ban_interest_allowable_expenditure,
        savings_ban_interest_taxable= (
            (financial_asset_income.savings_ban_interest_net_income + financial_asset_income.savings_ban_interest_tax_deduction_at_source) - 
            (financial_asset_income.savings_ban_interest_interest_on_loans + financial_asset_income.savings_ban_interest_allowable_expenditure)
            ),
        savings_ban_interest_description=financial_asset_income.savings_ban_interest_description,
        
        # Other Securities
        other_securities_net_income=financial_asset_income.other_securities_net_income,
        other_securities_tax_deduction_at_source=financial_asset_income.other_securities_tax_deduction_at_source,
        other_securities_interest_on_loans=financial_asset_income.other_securities_interest_on_loans,
        other_securities_allowable_expenditure=financial_asset_income.other_securities_allowable_expenditure,
        other_securities_taxable=(
            (financial_asset_income.other_securities_net_income + financial_asset_income.other_securities_tax_deduction_at_source) - 
            (financial_asset_income.other_securities_interest_on_loans + financial_asset_income.other_securities_allowable_expenditure)
            ),
        other_securities_description=financial_asset_income.other_securities_description,
        
        # Income from Islamic Principles
        income_from_islamic_principles_net_income=financial_asset_income.income_from_islamic_principles_net_income,
        income_from_islamic_principles_tax_deduction_at_source=financial_asset_income.income_from_islamic_principles_tax_deduction_at_source,
        income_from_islamic_principles_interest_on_loans=financial_asset_income.income_from_islamic_principles_interest_on_loans,
        income_from_islamic_principles_allowable_expenditure=financial_asset_income.income_from_islamic_principles_allowable_expenditure,
        income_from_islamic_principles_taxable=(
            (financial_asset_income.income_from_islamic_principles_net_income + financial_asset_income.income_from_islamic_principles_tax_deduction_at_source) - 
            (financial_asset_income.income_from_islamic_principles_interest_on_loans + financial_asset_income.income_from_islamic_principles_allowable_expenditure)
            ),
        income_from_islamic_principles_description=financial_asset_income.income_from_islamic_principles_description,
        
        # Bank Interest Savings Deposits
        bank_interest_savings_deposits_net_income=financial_asset_income.bank_interest_savings_deposits_net_income,
        bank_interest_savings_deposits_tax_deduction_at_source=financial_asset_income.bank_interest_savings_deposits_tax_deduction_at_source,
        bank_interest_savings_deposits_interest_on_loans=financial_asset_income.bank_interest_savings_deposits_interest_on_loans,
        bank_interest_savings_deposits_allowable_expenditure=financial_asset_income.bank_interest_savings_deposits_allowable_expenditure,
        bank_interest_savings_deposits_taxable=(
            (financial_asset_income.bank_interest_savings_deposits_net_income + financial_asset_income.bank_interest_savings_deposits_tax_deduction_at_source) - 
            (financial_asset_income.bank_interest_savings_deposits_interest_on_loans + financial_asset_income.bank_interest_savings_deposits_allowable_expenditure)
            ),
        bank_interest_savings_deposits_description=financial_asset_income.bank_interest_savings_deposits_description,
        
        # FDR Interest Income
        fdr_interest_income_net_income=financial_asset_income.fdr_interest_income_net_income,
        fdr_interest_income_tax_deduction_at_source=financial_asset_income.fdr_interest_income_tax_deduction_at_source,
        fdr_interest_income_interest_on_loans=financial_asset_income.fdr_interest_income_interest_on_loans,
        fdr_interest_income_allowable_expenditure=financial_asset_income.fdr_interest_income_allowable_expenditure,
        fdr_interest_income_taxable=(
            (financial_asset_income.fdr_interest_income_net_income + financial_asset_income.fdr_interest_income_tax_deduction_at_source) - 
            (financial_asset_income.fdr_interest_income_interest_on_loans + financial_asset_income.fdr_interest_income_allowable_expenditure)
            ),
        fdr_interest_income_description=financial_asset_income.fdr_interest_income_description,
        
        # Dividend Income
        dividend_income_net_income=financial_asset_income.dividend_income_net_income,
        dividend_income_tax_deduction_at_source=financial_asset_income.dividend_income_tax_deduction_at_source,
        dividend_income_interest_on_loans=financial_asset_income.dividend_income_interest_on_loans,
        dividend_income_allowable_expenditure=financial_asset_income.dividend_income_allowable_expenditure,
        dividend_income_taxable=(
            (financial_asset_income.dividend_income_net_income + financial_asset_income.dividend_income_tax_deduction_at_source) - 
            (financial_asset_income.dividend_income_interest_on_loans + financial_asset_income.dividend_income_allowable_expenditure)
            ),
        dividend_income_description=financial_asset_income.dividend_income_description,
        
        
        # total calculation
        total_net_income = (
            financial_asset_income.savings_ban_interest_net_income + 
            financial_asset_income.other_securities_net_income +
            financial_asset_income.income_from_islamic_principles_net_income + 
            financial_asset_income.bank_interest_savings_deposits_net_income + 
            financial_asset_income.fdr_interest_income_net_income + 
            financial_asset_income.dividend_income_net_income
            ),
        
        total_tax_deduction_at_source = (
            financial_asset_income.savings_ban_interest_tax_deduction_at_source +
            financial_asset_income.other_securities_tax_deduction_at_source +
            financial_asset_income.income_from_islamic_principles_tax_deduction_at_source +
            financial_asset_income.bank_interest_savings_deposits_tax_deduction_at_source +
            financial_asset_income.fdr_interest_income_tax_deduction_at_source +
            financial_asset_income.dividend_income_tax_deduction_at_source
            ),
        
        total_interest_on_loans = (
            financial_asset_income.savings_ban_interest_interest_on_loans +
            financial_asset_income.other_securities_interest_on_loans +
            financial_asset_income.income_from_islamic_principles_interest_on_loans +
            financial_asset_income.bank_interest_savings_deposits_interest_on_loans +
            financial_asset_income.fdr_interest_income_interest_on_loans +
            financial_asset_income.dividend_income_interest_on_loans
        ),
        
        total_allowable_expenditure = (
            financial_asset_income.savings_ban_interest_allowable_expenditure +
            financial_asset_income.other_securities_allowable_expenditure +
            financial_asset_income.income_from_islamic_principles_allowable_expenditure +
            financial_asset_income.bank_interest_savings_deposits_allowable_expenditure +
            financial_asset_income.fdr_interest_income_allowable_expenditure +
            financial_asset_income.dividend_income_allowable_expenditure
        ),

        
        total_taxable = (
            financial_asset_income.savings_ban_interest_net_income + financial_asset_income.other_securities_net_income +
            financial_asset_income.income_from_islamic_principles_net_income + financial_asset_income.bank_interest_savings_deposits_net_income + 
            financial_asset_income.fdr_interest_income_net_income + financial_asset_income.dividend_income_net_income +
            financial_asset_income.savings_ban_interest_tax_deduction_at_source + financial_asset_income.other_securities_tax_deduction_at_source +
            financial_asset_income.income_from_islamic_principles_tax_deduction_at_source + financial_asset_income.bank_interest_savings_deposits_tax_deduction_at_source + 
            financial_asset_income.fdr_interest_income_tax_deduction_at_source + financial_asset_income.dividend_income_tax_deduction_at_source -
            (
            financial_asset_income.savings_ban_interest_interest_on_loans + financial_asset_income.other_securities_interest_on_loans +
            financial_asset_income.income_from_islamic_principles_interest_on_loans + financial_asset_income.bank_interest_savings_deposits_interest_on_loans + 
            financial_asset_income.fdr_interest_income_interest_on_loans + financial_asset_income.dividend_income_interest_on_loans +
            financial_asset_income.savings_ban_interest_allowable_expenditure + financial_asset_income.other_securities_allowable_expenditure + 
            financial_asset_income.income_from_islamic_principles_allowable_expenditure + financial_asset_income.bank_interest_savings_deposits_allowable_expenditure + 
            financial_asset_income.fdr_interest_income_allowable_expenditure + financial_asset_income.dividend_income_allowable_expenditure
            )
        ),
        
 
        # Reduced Tax Rate Securities
        reduced_tax_rate_securities_net_income=financial_asset_income.reduced_tax_rate_securities_net_income,
        reduced_tax_rate_securities_tax_deduction_at_source=financial_asset_income.reduced_tax_rate_securities_tax_deduction_at_source,
        reduced_tax_rate_securities_interest_on_loans=financial_asset_income.reduced_tax_rate_securities_interest_on_loans,
        reduced_tax_rate_securities_allowable_expenditure=financial_asset_income.reduced_tax_rate_securities_allowable_expenditure,
        reduced_tax_rate_securities_taxable=(
            (financial_asset_income.reduced_tax_rate_securities_net_income + financial_asset_income.reduced_tax_rate_securities_tax_deduction_at_source) - 
            (financial_asset_income.reduced_tax_rate_securities_interest_on_loans + financial_asset_income.reduced_tax_rate_securities_allowable_expenditure)
        ),
        reduced_tax_rate_securities_description=financial_asset_income.reduced_tax_rate_securities_description,

        # Income from Other Resources
        income_other_resources_net_income=financial_asset_income.income_other_resources_net_income,
        income_other_resources_tax_deduction_at_source=financial_asset_income.income_other_resources_tax_deduction_at_source,
        income_other_resources_interest_on_loans=financial_asset_income.income_other_resources_interest_on_loans,
        income_other_resources_allowable_expenditure=financial_asset_income.income_other_resources_allowable_expenditure,
        income_other_resources_taxable=(
            (financial_asset_income.income_other_resources_net_income + financial_asset_income.income_other_resources_tax_deduction_at_source) - 
            (financial_asset_income.income_other_resources_interest_on_loans + financial_asset_income.income_other_resources_allowable_expenditure)
        ),
        income_other_resources_description=financial_asset_income.income_other_resources_description,

        # US Dollar Investment Bonds
        us_dollar_investment_bonds_net_income=financial_asset_income.us_dollar_investment_bonds_net_income,
        us_dollar_investment_bonds_tax_deduction_at_source=financial_asset_income.us_dollar_investment_bonds_tax_deduction_at_source,
        us_dollar_investment_bonds_interest_on_loans=financial_asset_income.us_dollar_investment_bonds_interest_on_loans,
        us_dollar_investment_bonds_exampted_amount = financial_asset_income.us_dollar_investment_bonds_net_income,
        us_dollar_investment_bonds_allowable_expenditure=financial_asset_income.us_dollar_investment_bonds_allowable_expenditure,
        us_dollar_investment_bonds_taxable=0,
        us_dollar_investment_bonds_description=financial_asset_income.us_dollar_investment_bonds_description,

        # Euro Premium Bonds
        euro_premium_bonds_net_income=financial_asset_income.euro_premium_bonds_net_income,
        euro_premium_bonds_tax_deduction_at_source=financial_asset_income.euro_premium_bonds_tax_deduction_at_source,
        euro_premium_bonds_interest_on_loans=financial_asset_income.euro_premium_bonds_interest_on_loans,
        euro_premium_bonds_exampted_amount=financial_asset_income.euro_premium_bonds_net_income,
        euro_premium_bonds_allowable_expenditure=financial_asset_income.euro_premium_bonds_allowable_expenditure,
        euro_premium_bonds_taxable=0,
        euro_premium_bonds_description=financial_asset_income.euro_premium_bonds_description,

        # Pound Sterling Premium Bonds
        pound_sterling_premium_bonds_net_income=financial_asset_income.pound_sterling_premium_bonds_net_income,
        pound_sterling_premium_bonds_tax_deduction_at_source=financial_asset_income.pound_sterling_premium_bonds_tax_deduction_at_source,
        pound_sterling_premium_bonds_interest_on_loans=financial_asset_income.pound_sterling_premium_bonds_interest_on_loans,
        pound_sterling_premium_bonds_exampted_amount=financial_asset_income.pound_sterling_premium_bonds_net_income,
        pound_sterling_premium_bonds_allowable_expenditure=financial_asset_income.pound_sterling_premium_bonds_allowable_expenditure,
        pound_sterling_premium_bonds_taxable=0,
        pound_sterling_premium_bonds_description=financial_asset_income.pound_sterling_premium_bonds_description,

        # US Dollar Premium Bonds
        us_dollar_premium_bonds_net_income=financial_asset_income.us_dollar_premium_bonds_net_income,
        us_dollar_premium_bonds_tax_deduction_at_source=financial_asset_income.us_dollar_premium_bonds_tax_deduction_at_source,
        us_dollar_premium_bonds_interest_on_loans=financial_asset_income.us_dollar_premium_bonds_interest_on_loans,
        us_dollar_premium_bonds_exampted_amount=financial_asset_income.us_dollar_premium_bonds_net_income,
        us_dollar_premium_bonds_allowable_expenditure=financial_asset_income.us_dollar_premium_bonds_allowable_expenditure,
        us_dollar_premium_bonds_taxable=0,
        us_dollar_premium_bonds_description=financial_asset_income.us_dollar_premium_bonds_description,

        # Wage Earners Development Bonds
        wage_earners_development_bonds_net_income=financial_asset_income.wage_earners_development_bonds_net_income,
        wage_earners_development_bonds_tax_deduction_at_source=financial_asset_income.wage_earners_development_bonds_tax_deduction_at_source,
        wage_earners_development_bonds_interest_on_loans=financial_asset_income.wage_earners_development_bonds_interest_on_loans,
        wage_earners_development_bonds_exampted_amount=financial_asset_income.wage_earners_development_bonds_net_income,
        wage_earners_development_bonds_allowable_expenditure=financial_asset_income.wage_earners_development_bonds_allowable_expenditure,
        wage_earners_development_bonds_taxable=0,
        wage_earners_development_bonds_description=financial_asset_income.wage_earners_development_bonds_description,

        # Euro Investment Bonds
        euro_investment_bonds_net_income=financial_asset_income.euro_investment_bonds_net_income,
        euro_investment_bonds_tax_deduction_at_source=financial_asset_income.euro_investment_bonds_tax_deduction_at_source,
        euro_investment_bonds_interest_on_loans=financial_asset_income.euro_investment_bonds_interest_on_loans,
        euro_investment_bonds_exampted_amount=financial_asset_income.euro_investment_bonds_net_income,
        euro_investment_bonds_allowable_expenditure=financial_asset_income.euro_investment_bonds_allowable_expenditure,
        euro_investment_bonds_taxable=0,
        euro_investment_bonds_description=financial_asset_income.euro_investment_bonds_description,
        

        # total gross calculation
        total_gross_income =  (
            financial_asset_income.savings_ban_interest_net_income + 
            financial_asset_income.other_securities_net_income +
            financial_asset_income.income_from_islamic_principles_net_income + 
            financial_asset_income.bank_interest_savings_deposits_net_income + 
            financial_asset_income.fdr_interest_income_net_income + 
            financial_asset_income.dividend_income_net_income + 
            financial_asset_income.savings_ban_interest_tax_deduction_at_source +
            financial_asset_income.other_securities_tax_deduction_at_source +
            financial_asset_income.income_from_islamic_principles_tax_deduction_at_source +
            financial_asset_income.bank_interest_savings_deposits_tax_deduction_at_source +
            financial_asset_income.fdr_interest_income_tax_deduction_at_source +
            financial_asset_income.dividend_income_tax_deduction_at_source + 
            financial_asset_income.reduced_tax_rate_securities_net_income + 
            financial_asset_income.reduced_tax_rate_securities_tax_deduction_at_source + 
            financial_asset_income.income_other_resources_net_income + 
            financial_asset_income.income_other_resources_tax_deduction_at_source
            ),
        
        total_gross_expense = (
            financial_asset_income.savings_ban_interest_interest_on_loans +
            financial_asset_income.other_securities_interest_on_loans +
            financial_asset_income.income_from_islamic_principles_interest_on_loans +
            financial_asset_income.bank_interest_savings_deposits_interest_on_loans +
            financial_asset_income.fdr_interest_income_interest_on_loans +
            financial_asset_income.dividend_income_interest_on_loans + 
            financial_asset_income.savings_ban_interest_allowable_expenditure +
            financial_asset_income.other_securities_allowable_expenditure +
            financial_asset_income.income_from_islamic_principles_allowable_expenditure +
            financial_asset_income.bank_interest_savings_deposits_allowable_expenditure +
            financial_asset_income.fdr_interest_income_allowable_expenditure +
            financial_asset_income.dividend_income_allowable_expenditure + 
            financial_asset_income.reduced_tax_rate_securities_interest_on_loans + 
            financial_asset_income.reduced_tax_rate_securities_allowable_expenditure + 
            financial_asset_income.income_other_resources_interest_on_loans + 
            financial_asset_income.income_other_resources_allowable_expenditure
            ),
        
        total_gross_exampted = (
            financial_asset_income.us_dollar_investment_bonds_net_income + 
            financial_asset_income.euro_premium_bonds_net_income + 
            financial_asset_income.pound_sterling_premium_bonds_net_income + 
            financial_asset_income.us_dollar_premium_bonds_net_income + 
            financial_asset_income.wage_earners_development_bonds_net_income + 
            financial_asset_income.euro_investment_bonds_net_income
            ),
        
        total_gross_taxable = (
            (
            financial_asset_income.savings_ban_interest_net_income + financial_asset_income.other_securities_net_income +
            financial_asset_income.income_from_islamic_principles_net_income + financial_asset_income.bank_interest_savings_deposits_net_income + 
            financial_asset_income.fdr_interest_income_net_income + financial_asset_income.dividend_income_net_income +
            financial_asset_income.savings_ban_interest_tax_deduction_at_source + financial_asset_income.other_securities_tax_deduction_at_source +
            financial_asset_income.income_from_islamic_principles_tax_deduction_at_source + financial_asset_income.bank_interest_savings_deposits_tax_deduction_at_source + 
            financial_asset_income.fdr_interest_income_tax_deduction_at_source + financial_asset_income.dividend_income_tax_deduction_at_source -
            (
            financial_asset_income.savings_ban_interest_interest_on_loans + financial_asset_income.other_securities_interest_on_loans +
            financial_asset_income.income_from_islamic_principles_interest_on_loans + financial_asset_income.bank_interest_savings_deposits_interest_on_loans + 
            financial_asset_income.fdr_interest_income_interest_on_loans + financial_asset_income.dividend_income_interest_on_loans +
            financial_asset_income.savings_ban_interest_allowable_expenditure + financial_asset_income.other_securities_allowable_expenditure + 
            financial_asset_income.income_from_islamic_principles_allowable_expenditure + financial_asset_income.bank_interest_savings_deposits_allowable_expenditure + 
            financial_asset_income.fdr_interest_income_allowable_expenditure + financial_asset_income.dividend_income_allowable_expenditure
            ) 
            )+ 
            (
            (financial_asset_income.reduced_tax_rate_securities_net_income + financial_asset_income.reduced_tax_rate_securities_tax_deduction_at_source) - 
            (financial_asset_income.reduced_tax_rate_securities_interest_on_loans + financial_asset_income.reduced_tax_rate_securities_allowable_expenditure)
            ) + 
            (
            (financial_asset_income.income_other_resources_net_income + financial_asset_income.income_other_resources_tax_deduction_at_source) - 
            (financial_asset_income.income_other_resources_interest_on_loans + financial_asset_income.income_other_resources_allowable_expenditure)
            )
        )
    )
    
    db.add(financial_asset_income)
    db.commit()
    db.refresh(financial_asset_income)
    return financial_asset_income



def update_financial_asset_income(db: Session, financial_asset_income: schemas.Financial_Asset_Income, petin: str):
    # Fetch the existing record by ETIN (or another unique identifier)
    existing_record = db.query(models.FinancialAssetIncome).filter(models.FinancialAssetIncome.etin == petin).first()
    
    if existing_record is None:
        raise ValueError(f"Record with ETIN {petin} not found")

    # Update the fields with new values from the provided financial_asset_income
    existing_record.savings_ban_interest_net_income = financial_asset_income.savings_ban_interest_net_income,
    existing_record.savings_ban_interest_tax_deduction_at_source = financial_asset_income.savings_ban_interest_tax_deduction_at_source,
    existing_record.savings_ban_interest_interest_on_loans = financial_asset_income.savings_ban_interest_interest_on_loans,
    existing_record.savings_ban_interest_allowable_expenditure = financial_asset_income.savings_ban_interest_allowable_expenditure,
    existing_record.savings_ban_interest_taxable = (
        (financial_asset_income.savings_ban_interest_net_income + financial_asset_income.savings_ban_interest_tax_deduction_at_source) - 
        (financial_asset_income.savings_ban_interest_interest_on_loans + financial_asset_income.savings_ban_interest_allowable_expenditure)
        ),
    existing_record.savings_ban_interest_description = financial_asset_income.savings_ban_interest_description,

    existing_record.other_securities_net_income = financial_asset_income.other_securities_net_income,
    existing_record.other_securities_tax_deduction_at_source = financial_asset_income.other_securities_tax_deduction_at_source,
    existing_record.other_securities_interest_on_loans = financial_asset_income.other_securities_interest_on_loans,
    existing_record.other_securities_allowable_expenditure = financial_asset_income.other_securities_allowable_expenditure,
    existing_record.other_securities_taxable = (
        (financial_asset_income.other_securities_net_income + financial_asset_income.other_securities_tax_deduction_at_source) - 
        (financial_asset_income.other_securities_interest_on_loans + financial_asset_income.other_securities_allowable_expenditure)
        ),
    existing_record.other_securities_description = financial_asset_income.other_securities_description,

    existing_record.income_from_islamic_principles_net_income = financial_asset_income.income_from_islamic_principles_net_income,
    existing_record.income_from_islamic_principles_tax_deduction_at_source = financial_asset_income.income_from_islamic_principles_tax_deduction_at_source,
    existing_record.income_from_islamic_principles_interest_on_loans = financial_asset_income.income_from_islamic_principles_interest_on_loans,
    existing_record.income_from_islamic_principles_allowable_expenditure = financial_asset_income.income_from_islamic_principles_allowable_expenditure,
    existing_record.income_from_islamic_principles_taxable = (
        (financial_asset_income.income_from_islamic_principles_net_income + financial_asset_income.income_from_islamic_principles_tax_deduction_at_source) - 
        (financial_asset_income.income_from_islamic_principles_interest_on_loans + financial_asset_income.income_from_islamic_principles_allowable_expenditure)
        ),
    existing_record.income_from_islamic_principles_description = financial_asset_income.income_from_islamic_principles_description,

    existing_record.bank_interest_savings_deposits_net_income = financial_asset_income.bank_interest_savings_deposits_net_income,
    existing_record.bank_interest_savings_deposits_tax_deduction_at_source = financial_asset_income.bank_interest_savings_deposits_tax_deduction_at_source,
    existing_record.bank_interest_savings_deposits_interest_on_loans = financial_asset_income.bank_interest_savings_deposits_interest_on_loans,
    existing_record.bank_interest_savings_deposits_allowable_expenditure = financial_asset_income.bank_interest_savings_deposits_allowable_expenditure,
    existing_record.bank_interest_savings_deposits_taxable = (
        (financial_asset_income.bank_interest_savings_deposits_net_income + financial_asset_income.bank_interest_savings_deposits_tax_deduction_at_source) - 
        (financial_asset_income.bank_interest_savings_deposits_interest_on_loans + financial_asset_income.bank_interest_savings_deposits_allowable_expenditure)
        ),
    existing_record.bank_interest_savings_deposits_description = financial_asset_income.bank_interest_savings_deposits_description,

    existing_record.fdr_interest_income_net_income = financial_asset_income.fdr_interest_income_net_income,
    existing_record.fdr_interest_income_tax_deduction_at_source = financial_asset_income.fdr_interest_income_tax_deduction_at_source,
    existing_record.fdr_interest_income_interest_on_loans = financial_asset_income.fdr_interest_income_interest_on_loans,
    existing_record.fdr_interest_income_allowable_expenditure = financial_asset_income.fdr_interest_income_allowable_expenditure,
    existing_record.fdr_interest_income_taxable = (
        (financial_asset_income.fdr_interest_income_net_income + financial_asset_income.fdr_interest_income_tax_deduction_at_source) - 
        (financial_asset_income.fdr_interest_income_interest_on_loans + financial_asset_income.fdr_interest_income_allowable_expenditure)
        ),
    existing_record.fdr_interest_income_description = financial_asset_income.fdr_interest_income_description,

    existing_record.dividend_income_net_income = financial_asset_income.dividend_income_net_income,
    existing_record.dividend_income_tax_deduction_at_source = financial_asset_income.dividend_income_tax_deduction_at_source,
    existing_record.dividend_income_interest_on_loans = financial_asset_income.dividend_income_interest_on_loans,
    existing_record.dividend_income_allowable_expenditure = financial_asset_income.dividend_income_allowable_expenditure,
    existing_record.dividend_income_taxable = (
        (financial_asset_income.dividend_income_net_income + financial_asset_income.dividend_income_tax_deduction_at_source) - 
        (financial_asset_income.dividend_income_interest_on_loans + financial_asset_income.dividend_income_allowable_expenditure)
        ),
    existing_record.dividend_income_description = financial_asset_income.dividend_income_description,
    
    
    
    
    existing_record.total_net_income = (
            financial_asset_income.savings_ban_interest_net_income + 
            financial_asset_income.other_securities_net_income +
            financial_asset_income.income_from_islamic_principles_net_income + 
            financial_asset_income.bank_interest_savings_deposits_net_income + 
            financial_asset_income.fdr_interest_income_net_income + 
            financial_asset_income.dividend_income_net_income
            ),
        
    existing_record.total_tax_deduction_at_source = (
        financial_asset_income.savings_ban_interest_tax_deduction_at_source +
        financial_asset_income.other_securities_tax_deduction_at_source +
        financial_asset_income.income_from_islamic_principles_tax_deduction_at_source +
        financial_asset_income.bank_interest_savings_deposits_tax_deduction_at_source +
        financial_asset_income.fdr_interest_income_tax_deduction_at_source +
        financial_asset_income.dividend_income_tax_deduction_at_source
        ),
    
    existing_record.total_interest_on_loans = (
        financial_asset_income.savings_ban_interest_interest_on_loans +
        financial_asset_income.other_securities_interest_on_loans +
        financial_asset_income.income_from_islamic_principles_interest_on_loans +
        financial_asset_income.bank_interest_savings_deposits_interest_on_loans +
        financial_asset_income.fdr_interest_income_interest_on_loans +
        financial_asset_income.dividend_income_interest_on_loans
    ),
    
    existing_record.total_allowable_expenditure = (
        financial_asset_income.savings_ban_interest_allowable_expenditure +
        financial_asset_income.other_securities_allowable_expenditure +
        financial_asset_income.income_from_islamic_principles_allowable_expenditure +
        financial_asset_income.bank_interest_savings_deposits_allowable_expenditure +
        financial_asset_income.fdr_interest_income_allowable_expenditure +
        financial_asset_income.dividend_income_allowable_expenditure
    ),

    existing_record.total_taxable = (
        financial_asset_income.savings_ban_interest_net_income + financial_asset_income.other_securities_net_income +
        financial_asset_income.income_from_islamic_principles_net_income + financial_asset_income.bank_interest_savings_deposits_net_income + 
        financial_asset_income.fdr_interest_income_net_income + financial_asset_income.dividend_income_net_income +
        financial_asset_income.savings_ban_interest_tax_deduction_at_source + financial_asset_income.other_securities_tax_deduction_at_source +
        financial_asset_income.income_from_islamic_principles_tax_deduction_at_source + financial_asset_income.bank_interest_savings_deposits_tax_deduction_at_source + 
        financial_asset_income.fdr_interest_income_tax_deduction_at_source + financial_asset_income.dividend_income_tax_deduction_at_source -
        (
        financial_asset_income.savings_ban_interest_interest_on_loans + financial_asset_income.other_securities_interest_on_loans +
        financial_asset_income.income_from_islamic_principles_interest_on_loans + financial_asset_income.bank_interest_savings_deposits_interest_on_loans + 
        financial_asset_income.fdr_interest_income_interest_on_loans + financial_asset_income.dividend_income_interest_on_loans +
        financial_asset_income.savings_ban_interest_allowable_expenditure + financial_asset_income.other_securities_allowable_expenditure + 
        financial_asset_income.income_from_islamic_principles_allowable_expenditure + financial_asset_income.bank_interest_savings_deposits_allowable_expenditure + 
        financial_asset_income.fdr_interest_income_allowable_expenditure + financial_asset_income.dividend_income_allowable_expenditure
        )
    ),
        

    

    existing_record.reduced_tax_rate_securities_net_income = financial_asset_income.reduced_tax_rate_securities_net_income,
    existing_record.reduced_tax_rate_securities_tax_deduction_at_source = financial_asset_income.reduced_tax_rate_securities_tax_deduction_at_source,
    existing_record.reduced_tax_rate_securities_interest_on_loans = financial_asset_income.reduced_tax_rate_securities_interest_on_loans,
    existing_record.reduced_tax_rate_securities_allowable_expenditure = financial_asset_income.reduced_tax_rate_securities_allowable_expenditure,
    existing_record.reduced_tax_rate_securities_taxable = (
        (financial_asset_income.reduced_tax_rate_securities_net_income + financial_asset_income.reduced_tax_rate_securities_tax_deduction_at_source) - 
        (financial_asset_income.reduced_tax_rate_securities_interest_on_loans + financial_asset_income.reduced_tax_rate_securities_allowable_expenditure)
        ),
    existing_record.reduced_tax_rate_securities_description = financial_asset_income.reduced_tax_rate_securities_description,

    existing_record.income_other_resources_net_income = financial_asset_income.income_other_resources_net_income,
    existing_record.income_other_resources_tax_deduction_at_source = financial_asset_income.income_other_resources_tax_deduction_at_source,
    existing_record.income_other_resources_interest_on_loans = financial_asset_income.income_other_resources_interest_on_loans,
    existing_record.income_other_resources_allowable_expenditure = financial_asset_income.income_other_resources_allowable_expenditure,
    existing_record.income_other_resources_taxable = (
        (financial_asset_income.income_other_resources_net_income + financial_asset_income.income_other_resources_tax_deduction_at_source) - 
        (financial_asset_income.income_other_resources_interest_on_loans + financial_asset_income.income_other_resources_allowable_expenditure)
        ),
    existing_record.income_other_resources_description = financial_asset_income.income_other_resources_description,

    existing_record.us_dollar_investment_bonds_net_income = financial_asset_income.us_dollar_investment_bonds_net_income,
    existing_record.us_dollar_investment_bonds_tax_deduction_at_source = financial_asset_income.us_dollar_investment_bonds_tax_deduction_at_source,
    existing_record.us_dollar_investment_bonds_interest_on_loans = financial_asset_income.us_dollar_investment_bonds_interest_on_loans,
    existing_record.us_dollar_investment_bonds_allowable_expenditure = financial_asset_income.us_dollar_investment_bonds_allowable_expenditure,
    existing_record.us_dollar_investment_bonds_taxable = 0,
    existing_record.us_dollar_investment_bonds_description = financial_asset_income.us_dollar_investment_bonds_description,

    existing_record.euro_premium_bonds_net_income = financial_asset_income.euro_premium_bonds_net_income,
    existing_record.euro_premium_bonds_tax_deduction_at_source = financial_asset_income.euro_premium_bonds_tax_deduction_at_source,
    existing_record.euro_premium_bonds_interest_on_loans = financial_asset_income.euro_premium_bonds_interest_on_loans,
    existing_record.euro_premium_bonds_allowable_expenditure = financial_asset_income.euro_premium_bonds_allowable_expenditure,
    existing_record.euro_premium_bonds_taxable = 0,
    existing_record.euro_premium_bonds_description = financial_asset_income.euro_premium_bonds_description,

    existing_record.pound_sterling_premium_bonds_net_income = financial_asset_income.pound_sterling_premium_bonds_net_income,
    existing_record.pound_sterling_premium_bonds_tax_deduction_at_source = financial_asset_income.pound_sterling_premium_bonds_tax_deduction_at_source,
    existing_record.pound_sterling_premium_bonds_interest_on_loans = financial_asset_income.pound_sterling_premium_bonds_interest_on_loans,
    existing_record.pound_sterling_premium_bonds_allowable_expenditure = financial_asset_income.pound_sterling_premium_bonds_allowable_expenditure,
    existing_record.pound_sterling_premium_bonds_taxable = 0,
    existing_record.pound_sterling_premium_bonds_description = financial_asset_income.pound_sterling_premium_bonds_description,

    existing_record.us_dollar_premium_bonds_net_income = financial_asset_income.us_dollar_premium_bonds_net_income,
    existing_record.us_dollar_premium_bonds_tax_deduction_at_source = financial_asset_income.us_dollar_premium_bonds_tax_deduction_at_source,
    existing_record.us_dollar_premium_bonds_interest_on_loans = financial_asset_income.us_dollar_premium_bonds_interest_on_loans,
    existing_record.us_dollar_premium_bonds_allowable_expenditure = financial_asset_income.us_dollar_premium_bonds_allowable_expenditure,
    existing_record.us_dollar_premium_bonds_taxable = 0,
    existing_record.us_dollar_premium_bonds_description = financial_asset_income.us_dollar_premium_bonds_description,

    existing_record.wage_earners_development_bonds_net_income = financial_asset_income.wage_earners_development_bonds_net_income,
    existing_record.wage_earners_development_bonds_tax_deduction_at_source = financial_asset_income.wage_earners_development_bonds_tax_deduction_at_source,
    existing_record.wage_earners_development_bonds_interest_on_loans = financial_asset_income.wage_earners_development_bonds_interest_on_loans,
    existing_record.wage_earners_development_bonds_allowable_expenditure = financial_asset_income.wage_earners_development_bonds_allowable_expenditure,
    existing_record.wage_earners_development_bonds_taxable = 0,
    existing_record.wage_earners_development_bonds_description = financial_asset_income.wage_earners_development_bonds_description,

    existing_record.euro_investment_bonds_net_income = financial_asset_income.euro_investment_bonds_net_income,
    existing_record.euro_investment_bonds_tax_deduction_at_source = financial_asset_income.euro_investment_bonds_tax_deduction_at_source,
    existing_record.euro_investment_bonds_interest_on_loans = financial_asset_income.euro_investment_bonds_interest_on_loans,
    existing_record.euro_investment_bonds_allowable_expenditure = financial_asset_income.euro_investment_bonds_allowable_expenditure,
    existing_record.euro_investment_bonds_taxable = 0,
    existing_record.euro_investment_bonds_description = financial_asset_income.euro_investment_bonds_description,
    
    existing_record.total_gross_income =  (
        financial_asset_income.savings_ban_interest_net_income + 
        financial_asset_income.other_securities_net_income +
        financial_asset_income.income_from_islamic_principles_net_income + 
        financial_asset_income.bank_interest_savings_deposits_net_income + 
        financial_asset_income.fdr_interest_income_net_income + 
        financial_asset_income.dividend_income_net_income + 
        financial_asset_income.savings_ban_interest_tax_deduction_at_source +
        financial_asset_income.other_securities_tax_deduction_at_source +
        financial_asset_income.income_from_islamic_principles_tax_deduction_at_source +
        financial_asset_income.bank_interest_savings_deposits_tax_deduction_at_source +
        financial_asset_income.fdr_interest_income_tax_deduction_at_source +
        financial_asset_income.dividend_income_tax_deduction_at_source + 
        financial_asset_income.reduced_tax_rate_securities_net_income + 
        financial_asset_income.reduced_tax_rate_securities_tax_deduction_at_source + 
        financial_asset_income.income_other_resources_net_income + 
        financial_asset_income.income_other_resources_tax_deduction_at_source
        ),
    
    existing_record.total_gross_expense = (
        financial_asset_income.savings_ban_interest_interest_on_loans +
        financial_asset_income.other_securities_interest_on_loans +
        financial_asset_income.income_from_islamic_principles_interest_on_loans +
        financial_asset_income.bank_interest_savings_deposits_interest_on_loans +
        financial_asset_income.fdr_interest_income_interest_on_loans +
        financial_asset_income.dividend_income_interest_on_loans + 
        financial_asset_income.savings_ban_interest_allowable_expenditure +
        financial_asset_income.other_securities_allowable_expenditure +
        financial_asset_income.income_from_islamic_principles_allowable_expenditure +
        financial_asset_income.bank_interest_savings_deposits_allowable_expenditure +
        financial_asset_income.fdr_interest_income_allowable_expenditure +
        financial_asset_income.dividend_income_allowable_expenditure + 
        financial_asset_income.reduced_tax_rate_securities_interest_on_loans + 
        financial_asset_income.reduced_tax_rate_securities_allowable_expenditure + 
        financial_asset_income.income_other_resources_interest_on_loans + 
        financial_asset_income.income_other_resources_allowable_expenditure
        ),
    
    existing_record.total_gross_exampted = (
        financial_asset_income.us_dollar_investment_bonds_net_income + 
        financial_asset_income.euro_premium_bonds_net_income + 
        financial_asset_income.pound_sterling_premium_bonds_net_income + 
        financial_asset_income.us_dollar_premium_bonds_net_income + 
        financial_asset_income.wage_earners_development_bonds_net_income + 
        financial_asset_income.euro_investment_bonds_net_income
        ),
    
    existing_record.total_gross_taxable = (
        (
        financial_asset_income.savings_ban_interest_net_income + financial_asset_income.other_securities_net_income +
        financial_asset_income.income_from_islamic_principles_net_income + financial_asset_income.bank_interest_savings_deposits_net_income + 
        financial_asset_income.fdr_interest_income_net_income + financial_asset_income.dividend_income_net_income +
        financial_asset_income.savings_ban_interest_tax_deduction_at_source + financial_asset_income.other_securities_tax_deduction_at_source +
        financial_asset_income.income_from_islamic_principles_tax_deduction_at_source + financial_asset_income.bank_interest_savings_deposits_tax_deduction_at_source + 
        financial_asset_income.fdr_interest_income_tax_deduction_at_source + financial_asset_income.dividend_income_tax_deduction_at_source -
        (
        financial_asset_income.savings_ban_interest_interest_on_loans + financial_asset_income.other_securities_interest_on_loans +
        financial_asset_income.income_from_islamic_principles_interest_on_loans + financial_asset_income.bank_interest_savings_deposits_interest_on_loans + 
        financial_asset_income.fdr_interest_income_interest_on_loans + financial_asset_income.dividend_income_interest_on_loans +
        financial_asset_income.savings_ban_interest_allowable_expenditure + financial_asset_income.other_securities_allowable_expenditure + 
        financial_asset_income.income_from_islamic_principles_allowable_expenditure + financial_asset_income.bank_interest_savings_deposits_allowable_expenditure + 
        financial_asset_income.fdr_interest_income_allowable_expenditure + financial_asset_income.dividend_income_allowable_expenditure
        ) 
        )+ 
        (
        (financial_asset_income.reduced_tax_rate_securities_net_income + financial_asset_income.reduced_tax_rate_securities_tax_deduction_at_source) - 
        (financial_asset_income.reduced_tax_rate_securities_interest_on_loans + financial_asset_income.reduced_tax_rate_securities_allowable_expenditure)
        ) + 
        (
        (financial_asset_income.income_other_resources_net_income + financial_asset_income.income_other_resources_tax_deduction_at_source) - 
        (financial_asset_income.income_other_resources_interest_on_loans + financial_asset_income.income_other_resources_allowable_expenditure)
        )
    )

    

    # Commit the changes to the database
    db.commit()
    db.refresh(existing_record)
    return existing_record





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
    return db.query(models.TaxRecord).filter(models.TaxRecord.etin == etin).first()

def get_tax_records(db: Session, skip: int , limit: int):
    return db.query(models.TaxRecord).offset(skip).limit(limit).all()


def create_tax_record(db: Session, petin : str, net_tax_liability : int, area_tax : int, min_tax:int, actual_payable_tax : int):
    tax_record = models.TaxRecord(
        etin = petin,
        net_tax_liability=net_tax_liability,
        min_tax=min_tax,
        area_tax=area_tax,
        actual_payable_tax=actual_payable_tax
    )
    
    db.add(tax_record)
    db.commit()
    db.refresh(tax_record)
    return tax_record
