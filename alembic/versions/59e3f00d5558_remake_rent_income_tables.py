"""remake rent income tables

Revision ID: 59e3f00d5558
Revises: cd3548fefffe
Create Date: 2024-12-12 17:11:16.907551

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '59e3f00d5558'
down_revision: Union[str, None] = 'cd3548fefffe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None




def upgrade() -> None:
    # Drop the RentIncomeDetails table
    op.drop_table('rent_income_details')

    # Drop the RentIncomeMaster table
    op.drop_table('rent_income_master')

    
def downgrade() -> None:
    # Recreate the RentIncomeDetails table
    op.create_table(
        'rent_income_details',
        sa.Column('id', sa.Integer, primary_key=True, index=True, unique=True),
        sa.Column('area_type', sa.String(length=50), nullable=True),  # Adjust type as needed
        sa.Column('asset_name', sa.String(length=100), nullable=False),
        sa.Column('asset_address', sa.String(length=500), nullable=False),
        sa.Column('total_income', sa.Integer, default=0),
        sa.Column('total_expense', sa.Integer, default=0),
        sa.Column('special_income', sa.Integer, default=0),
        sa.Column('net_income', sa.Integer, default=0),
        sa.Column('rent_taken', sa.Integer, default=0),
        sa.Column('yearly_value', sa.Integer, default=0),
        sa.Column('other_charge', sa.Integer, default=0),
        sa.Column('other_taken_rent', sa.Integer, default=0),
        sa.Column('vacancy_allowance', sa.Integer, default=0),
        sa.Column('insurance_premium_paid_actual', sa.Integer, default=0),
        sa.Column('insurance_premium_paid_allowable', sa.Integer, default=0),
        sa.Column('interest_on_repaid_loans_actual', sa.Integer, default=0),
        sa.Column('interest_on_repaid_loans_allowable', sa.Integer, default=0),
        sa.Column('land_revenue_actual', sa.Integer, default=0),
        sa.Column('land_revenue_allowable', sa.Integer, default=0),
        sa.Column('municipal_or_local_tax_actual', sa.Integer, default=0),
        sa.Column('municipal_or_local_tax_allowable', sa.Integer, default=0),
        sa.Column('receipt_of_repairs_actual', sa.Integer, default=0),
        sa.Column('receipt_of_repairs_allowable', sa.Integer, default=0),
        sa.Column('etin', sa.String(length=12), nullable=False)
    )

    # Recreate the RentIncomeMaster table
    op.create_table(
        'rent_income_master',
        sa.Column('id', sa.Integer, primary_key=True, index=True, unique=True),
        sa.Column('space_type', sa.String(length=100), nullable=False),
        sa.Column('live_ownself', sa.String(length=50), nullable=True),  # Adjust type as needed
        sa.Column('monthly_rent', sa.Integer, default=0),
        sa.Column('monthly_service_charge', sa.Integer, default=0),
        sa.Column('advance', sa.Integer, default=0),
        sa.Column('adjusted_rent', sa.Integer, default=0),
        sa.Column('all_month', sa.String(length=50), nullable=True),  # Adjust type as needed
        sa.Column('total_rent', sa.Integer, default=0),
        sa.Column('total_rent_received', sa.Integer, default=0),
        sa.Column('total_service_charge_received', sa.Integer, default=0),
        sa.Column('total_vacancy_rent', sa.Integer, default=0),
        sa.Column('total_vacancy_month', sa.Integer, default=0),
        sa.Column('adjusted_advance', sa.Integer, default=0),
        sa.Column('etin', sa.String(length=12), nullable=False)
    )

    # Recreate the RentIncomeSummary table
    op.create_table(
        'rent_income_summary',
        sa.Column('id', sa.Integer, primary_key=True, index=True, unique=True),
        sa.Column('area_type', sa.String(length=50), nullable=True),  # Adjust type as needed
        sa.Column('asset_name', sa.String(length=100), nullable=False),
        sa.Column('asset_address', sa.String(length=500), nullable=False),
        sa.Column('gross_total_income', sa.Integer, default=0),
        sa.Column('gross_total_expense', sa.Integer, default=0),
        sa.Column('gross_net_income', sa.Integer, default=0),
        sa.Column('etin', sa.String(length=12), nullable=False)
    )