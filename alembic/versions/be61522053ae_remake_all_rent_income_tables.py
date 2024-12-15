"""remake all rent income tables

Revision ID: be61522053ae
Revises: 59e3f00d5558
Create Date: 2024-12-12 17:41:04.543699

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'be61522053ae'
down_revision: Union[str, None] = '59e3f00d5558'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    # Create ENUM types if they do not already exist
    enum_areatype = sa.dialects.postgresql.ENUM('residential', 'business', 'other', name='areatype', create_type=False)
    enum_liveownself = sa.dialects.postgresql.ENUM('yes', 'no', name='liveownself', create_type=False)
    enum_months = sa.dialects.postgresql.ENUM('yes', 'no', name='months', create_type=False)
    
    # Create the ENUMs explicitly if not already present
    op.execute("DO $$ BEGIN IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'areatype') THEN CREATE TYPE areatype AS ENUM ('residential', 'business', 'other'); END IF; END $$;")
    op.execute("DO $$ BEGIN IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'liveownself') THEN CREATE TYPE liveownself AS ENUM ('yes', 'no'); END IF; END $$;")
    op.execute("DO $$ BEGIN IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'months') THEN CREATE TYPE months AS ENUM ('yes', 'no'); END IF; END $$;")
    
    # Create rent_income_master table
    op.create_table(
        'rent_income_master',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('area_type', enum_areatype, nullable=True),
        sa.Column('asset_name', sa.String(length=100), nullable=False),
        sa.Column('asset_address', sa.String(length=500), nullable=False),
        sa.Column('total_income', sa.Integer(), nullable=True),
        sa.Column('total_expense', sa.Integer(), nullable=True),
        sa.Column('special_income', sa.Integer(), nullable=True),
        sa.Column('net_income', sa.Integer(), nullable=True),
        sa.Column('rent_taken', sa.Integer(), nullable=True),
        sa.Column('yearly_value', sa.Integer(), nullable=True),
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
        sa.Column('etin', sa.String(length=12), nullable=False),
        sa.ForeignKeyConstraint(['etin'], ['taxpayer.etin'], ),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Create rent_income_details table
    op.create_table(
        'rent_income_details',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('space_type', sa.String(length=100), nullable=False),
        sa.Column('live_ownself', enum_liveownself, nullable=True),
        sa.Column('monthly_rent', sa.Integer(), nullable=True),
        sa.Column('monthly_service_charge', sa.Integer(), nullable=True),
        sa.Column('advance', sa.Integer(), nullable=True),
        sa.Column('adjusted_rent', sa.Integer(), nullable=True),
        sa.Column('all_month', enum_months, nullable=True),
        sa.Column('january', enum_months, nullable=True),
        sa.Column('february', enum_months, nullable=True),
        sa.Column('march', enum_months, nullable=True),
        sa.Column('april', enum_months, nullable=True),
        sa.Column('may', enum_months, nullable=True),
        sa.Column('june', enum_months, nullable=True),
        sa.Column('july', enum_months, nullable=True),
        sa.Column('august', enum_months, nullable=True),
        sa.Column('september', enum_months, nullable=True),
        sa.Column('october', enum_months, nullable=True),
        sa.Column('november', enum_months, nullable=True),
        sa.Column('december', enum_months, nullable=True),
        sa.Column('total_rent', sa.Integer(), nullable=True),
        sa.Column('total_rent_received', sa.Integer(), nullable=True),
        sa.Column('total_service_charge_received', sa.Integer(), nullable=True),
        sa.Column('total_vacancy_rent', sa.Integer(), nullable=True),
        sa.Column('total_vacancy_month', sa.Integer(), nullable=True),
        sa.Column('adjusted_advance', sa.Integer(), nullable=True),
        sa.Column('etin', sa.String(length=12), nullable=False),
        sa.ForeignKeyConstraint(['etin'], ['taxpayer.etin'], ),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Create rent_income_summary table if it doesn't exist
    op.execute("""
        DO $$ 
        BEGIN 
            IF NOT EXISTS (SELECT 1 FROM pg_tables WHERE tablename = 'rent_income_summary') THEN
                CREATE TABLE rent_income_summary (
                    id SERIAL NOT NULL,
                    area_type VARCHAR(20),
                    asset_name VARCHAR(100) NOT NULL,
                    asset_address VARCHAR(500) NOT NULL,
                    gross_total_income INTEGER,
                    gross_total_expense INTEGER,
                    gross_net_income INTEGER,
                    etin VARCHAR(12) NOT NULL,
                    PRIMARY KEY (id),
                    FOREIGN KEY(etin) REFERENCES taxpayer (etin)
                );
            END IF;
        END $$;
    """)

    # Create index only if it doesn't exist
    op.execute("""
        DO $$ 
        BEGIN
            IF NOT EXISTS (SELECT 1 FROM pg_indexes WHERE indexname = 'ix_rent_income_summary_id') THEN
                CREATE UNIQUE INDEX ix_rent_income_summary_id ON rent_income_summary (id);
            END IF;
        END $$;
    """)
    
    # Create indexes AFTER the tables have been created
    op.create_index(op.f('ix_rent_income_master_id'), 'rent_income_master', ['id'], unique=True)
    op.create_index(op.f('ix_rent_income_details_id'), 'rent_income_details', ['id'], unique=True)





def downgrade() -> None:
    # Drop indexes first in reverse order of creation
    op.execute("DO $$ BEGIN IF EXISTS (SELECT 1 FROM pg_indexes WHERE tablename = 'rent_income_summary' AND indexname = 'ix_rent_income_summary_id') THEN DROP INDEX ix_rent_income_summary_id; END IF; END $$;")
    op.execute("DO $$ BEGIN IF EXISTS (SELECT 1 FROM pg_indexes WHERE tablename = 'rent_income_master' AND indexname = 'ix_rent_income_master_id') THEN DROP INDEX ix_rent_income_master_id; END IF; END $$;")
    op.execute("DO $$ BEGIN IF EXISTS (SELECT 1 FROM pg_indexes WHERE tablename = 'rent_income_details' AND indexname = 'ix_rent_income_details_id') THEN DROP INDEX ix_rent_income_details_id; END IF; END $$;")

    # Drop the tables in reverse order of creation, also ensuring they exist
    op.execute("DO $$ BEGIN IF EXISTS (SELECT 1 FROM pg_tables WHERE tablename = 'rent_income_summary') THEN DROP TABLE rent_income_summary; END IF; END $$;")
    op.execute("DO $$ BEGIN IF EXISTS (SELECT 1 FROM pg_tables WHERE tablename = 'rent_income_master') THEN DROP TABLE rent_income_master; END IF; END $$;")
    op.execute("DO $$ BEGIN IF EXISTS (SELECT 1 FROM pg_tables WHERE tablename = 'rent_income_details') THEN DROP TABLE rent_income_details; END IF; END $$;")

    # Drop ENUM types if they exist
    op.execute("DO $$ BEGIN IF EXISTS (SELECT 1 FROM pg_type WHERE typname = 'months') THEN DROP TYPE months; END IF; END $$;")
    op.execute("DO $$ BEGIN IF EXISTS (SELECT 1 FROM pg_type WHERE typname = 'liveownself') THEN DROP TYPE liveownself; END IF; END $$;")
    op.execute("DO $$ BEGIN IF EXISTS (SELECT 1 FROM pg_type WHERE typname = 'areatype') THEN DROP TYPE areatype; END IF; END $$;")