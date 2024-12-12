"""create rent income master table

Revision ID: cd3548fefffe
Revises: 
Create Date: 2024-12-12 14:05:51.760675

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import ENUM

# revision identifiers, used by Alembic.
revision: str = 'cd3548fefffe'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### Check and create ENUM types ###
    op.execute("""
    DO $$ BEGIN
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'areatype') THEN
            CREATE TYPE areatype AS ENUM ('residential', 'business', 'other');
        END IF;
    END $$;
    """)

    op.execute("""
    DO $$ BEGIN
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'liveownself') THEN
            CREATE TYPE liveownself AS ENUM ('yes', 'no');
        END IF;
    END $$;
    """)

    op.execute("""
    DO $$ BEGIN
        IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'months') THEN
            CREATE TYPE months AS ENUM ('yes', 'no');
        END IF;
    END $$;
    """)

    # ### Create Tables ###
    op.create_table('rent_income_details',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('area_type', ENUM('residential', 'business', 'other', name='areatype', create_type=False), nullable=True),
        sa.Column('asset_name', sa.String(length=100), nullable=False),
        sa.Column('asset_address', sa.String(length=500), nullable=False),
        sa.Column('total_income', sa.Integer(), nullable=True),
        sa.Column('total_expense', sa.Integer(), nullable=True),
        sa.Column('special_income', sa.Integer(), nullable=True),
        sa.Column('net_income', sa.Integer(), nullable=True),
        sa.Column('rent_taken', sa.Integer(), nullable=True),
        sa.Column('yearly_value', sa.Integer(), nullable=True),
        sa.Column('adjusted_advance', sa.Integer(), nullable=True),
        sa.Column('other_charge', sa.Integer(), nullable=True),
        sa.Column('other_taken_rent', sa.Integer(), nullable=True),
        sa.Column('vacancy_allowance', sa.Integer(), nullable=True),
        sa.Column('insurance_premium_paid_actual', sa.Integer(), nullable=True),
        sa.Column('insurance_premium_paid_allowable', sa.Integer(), nullable=True),
        sa.Column('interest_on_repaid_loans_actual', sa.Integer(), nullable=True),
        sa.Column('interest_on_repaid_loans_allowable', sa.Integer(), nullable=True),
        sa.Column('land_revenue_actual', sa.Integer(), nullable=True),
        sa.Column('land_revenue_allowable', sa.Integer(), nullable=True),
        sa.Column('municipal_or_local_tax_actual', sa.Integer(), nullable=True),
        sa.Column('municipal_or_local_tax_allowable', sa.Integer(), nullable=True),
        sa.Column('receipt_of_repairs_actual', sa.Integer(), nullable=True),
        sa.Column('receipt_of_repairs_allowable', sa.Integer(), nullable=True),
        sa.Column('space_type', sa.String(length=100), nullable=False),
        sa.Column('live_ownself', ENUM('yes', 'no', name='liveownself', create_type=False), nullable=True),
        sa.Column('monthly_rent', sa.Integer(), nullable=True),
        sa.Column('monthly_service_charge', sa.Integer(), nullable=True),
        sa.Column('advance', sa.Integer(), nullable=True),
        sa.Column('adjusted_rent', sa.Integer(), nullable=True),
        sa.Column('total_rent', sa.Integer(), nullable=True),
        sa.Column('total_rent_received', sa.Integer(), nullable=True),
        sa.Column('total_service_charge_received', sa.Integer(), nullable=True),
        sa.Column('total_vacancy_rent', sa.Integer(), nullable=True),
        sa.Column('total_vacancy_month', sa.Integer(), nullable=True),
        sa.Column('january', ENUM('yes', 'no', name='months', create_type=False), nullable=True),
        sa.Column('february', ENUM('yes', 'no', name='months', create_type=False), nullable=True),
        sa.Column('march', ENUM('yes', 'no', name='months', create_type=False), nullable=True),
        sa.Column('april', ENUM('yes', 'no', name='months', create_type=False), nullable=True),
        sa.Column('may', ENUM('yes', 'no', name='months', create_type=False), nullable=True),
        sa.Column('june', ENUM('yes', 'no', name='months', create_type=False), nullable=True),
        sa.Column('july', ENUM('yes', 'no', name='months', create_type=False), nullable=True),
        sa.Column('august', ENUM('yes', 'no', name='months', create_type=False), nullable=True),
        sa.Column('september', ENUM('yes', 'no', name='months', create_type=False), nullable=True),
        sa.Column('october', ENUM('yes', 'no', name='months', create_type=False), nullable=True),
        sa.Column('november', ENUM('yes', 'no', name='months', create_type=False), nullable=True),
        sa.Column('december', ENUM('yes', 'no', name='months', create_type=False), nullable=True),
        sa.Column('etin', sa.String(length=12), nullable=False),
        sa.ForeignKeyConstraint(['etin'], ['taxpayer.etin'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_rent_income_details_id'), 'rent_income_details', ['id'], unique=True)

    op.create_table('rent_income_master',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('area_type', ENUM('residential', 'business', 'other', name='areatype', create_type=False), nullable=True),
        sa.Column('asset_name', sa.String(length=100), nullable=False),
        sa.Column('asset_address', sa.String(length=500), nullable=False),
        sa.Column('gross_total_income', sa.Integer(), nullable=True),
        sa.Column('gross_total_expense', sa.Integer(), nullable=True),
        sa.Column('gross_net_income', sa.Integer(), nullable=True),
        sa.Column('etin', sa.String(length=12), nullable=False),
        sa.ForeignKeyConstraint(['etin'], ['taxpayer.etin'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_rent_income_master_id'), 'rent_income_master', ['id'], unique=True)




def downgrade() -> None:
    # ### Revert ENUM types ###


    op.drop_index(op.f('ix_rent_income_master_id'), table_name='rent_income_master')
    op.drop_table('rent_income_master')

    op.drop_index(op.f('ix_rent_income_details_id'), table_name='rent_income_details')
    op.drop_table('rent_income_details')