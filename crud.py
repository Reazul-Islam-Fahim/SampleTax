from sqlalchemy.orm import Session
import models, schemas

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




def get_private_salary_income_record(db: Session, etin: int):
    return db.query(models.PrivateSalaryIncomeRecord).filter(models.PrivateSalaryIncomeRecord.etin == etin).first()

def get_private_salary_income_records(db: Session, skip: int , limit: int):
    return db.query(models.PrivateSalaryIncomeRecord).offset(skip).limit(limit).all()


def create_private_salary_income_record(db: Session, private_salary: schemas.PrivateSalary_IncomeRecord):
    private_salary_income_records = models.PrivateSalaryIncomeRecord(
        id=private_salary.id,
        basic_salary=private_salary.basic_salary,
        house_rent_allowance=private_salary.house_rent_allowance,
        medical_allowance=private_salary.medical_allowance,
        festival_bonus=private_salary.festival_bonus,
        rent_free_accommodation=private_salary.rent_free_accommodation,
        accommodation_at_concessional_rate=private_salary.accommodation_at_concessional_rate,
        rent_paid_by_taxpayer=private_salary.rent_paid_by_taxpayer,
        vehicle_facility_months=private_salary.vehicle_facility_months,
        is_higher_cc=private_salary.is_higher_cc,
        other_non_cash_benefits=private_salary.other_non_cash_benefits,
        num_autistic_children=private_salary.num_autistic_children,
        arrear_salary=private_salary.arrear_salary,
        education_allowance=private_salary.education_allowance,
        entertainment_allowance=private_salary.entertainment_allowance,
        employer_contribution_RPF=private_salary.employer_contribution_RPF,
        gratuity=private_salary.gratuity,
        interest_accrued_RPF=private_salary.interest_accrued_RPF,
        leave_allowance=private_salary.leave_allowance,
        other_bonus=private_salary.other_bonus,
        overtime=private_salary.overtime_bonus,
        pension=private_salary.pension,
        tada=private_salary.tada,
        income_from_employee_share_scheme=private_salary.income_from_employee_share_scheme,
        others=private_salary.others,
        allowances=private_salary.allowances,
        perquisites=private_salary.perquisites,
        etin=private_salary.etin
    )
    
    db.add(private_salary_income_records)
    db.commit()
    db.refresh(private_salary_income_records)
    return private_salary_income_records




def get_gov_salary_income_record(db: Session, etin: int):
    return db.query(models.GovSalaryIncomeRecord).filter(models.GovSalaryIncomeRecord.etin == etin).first()

def get_gov_salary_income_records(db: Session, skip: int , limit: int):
    return db.query(models.GovSalaryIncomeRecord).offset(skip).limit(limit).all()


def create_gov_salary_income_record(db: Session, gov_salary: schemas.GovSalary_IncomeRecord):
    gov_salary_income_records = models.GovSalaryIncomeRecord(
        id=gov_salary.id,
        basic_salary=gov_salary.basic_salary,
        house_rent_allowance=gov_salary.house_rent_allowance,
        medical_allowance=gov_salary.medical_allowance,
        festival_bonus=gov_salary.festival_bonus,
        arrear_pay=gov_salary.arrear_pay,
        special_allowance=gov_salary.special_allowance,
        conveyance_allowance=gov_salary.conveyance_allowance,
        support_staff_allowance=gov_salary.support_staff_allowance,
        leave_allowance=gov_salary.leave_allowance,
        reward=gov_salary.reward,
        overtime=gov_salary.overtime,
        bangla_noboborsho=gov_salary.bangla_noboborsho,
        interest_accrued_from_PF=gov_salary.interest_accrued_from_PF,
        lump_grant=gov_salary.lump_grant,
        gratuity=gov_salary.gratuity,
        others=gov_salary.others,
        etin=gov_salary.etin
    )
    
    db.add(gov_salary_income_records)
    db.commit()
    db.refresh(gov_salary_income_records)
    return gov_salary_income_records





def get_salary_income_summery(db: Session, etin: int):
    return db.query(models.SalaryIncomeSummery).filter(models.SalaryIncomeSummery.etin == etin).first()

def get_salary_income_summerys(db: Session, skip: int , limit: int):
    return db.query(models.SalaryIncomeSummery).offset(skip).limit(limit).all()


def create_salary_income_summery(db: Session, salary_summery: schemas.SalaryIncome_Summery):
    salary_income_summery = models.SalaryIncomeSummery(
        etin = salary_summery.etin,
        total_income=salary_summery.total_income,
        exempted_income=salary_summery.exempted_income,
        taxable_income=salary_summery.taxable_income,
        tax_liability=salary_summery.tax_liability,
        
    )
    
    db.add(salary_income_summery)
    db.commit()
    db.refresh(salary_income_summery)
    return salary_income_summery