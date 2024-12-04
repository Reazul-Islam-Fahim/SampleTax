"""change column name in taxpayer and column type in financial assetes

Revision ID: 7614ab5483bd
Revises: a7b43268149a
Create Date: 2024-12-04 17:56:50.452444

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7614ab5483bd'
down_revision: Union[str, None] = 'a7b43268149a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('taxpayer', 'address', new_column_name='permanant_address')

    # op.alter_column('financial_asset_income', 'other_securities_net_income', existing_type=sa.String(), type_=sa.Integer(), server_default='0')
    
    op.execute(
        """
        ALTER TABLE financial_asset_income
        ALTER COLUMN other_securities_net_income DROP DEFAULT
        """
    )

    # Change column type of 'other_securities_net_income' from String to Integer with explicit casting
    op.execute(
        """
        ALTER TABLE financial_asset_income
        ALTER COLUMN other_securities_net_income TYPE INTEGER
        USING other_securities_net_income::integer
        """
    )

    # Set a new default value for the column
    op.execute(
        """
        ALTER TABLE financial_asset_income
        ALTER COLUMN other_securities_net_income SET DEFAULT 0
        """
    )

def downgrade():
    op.alter_column('taxpayer', 'permanant_address', new_column_name='address')

    # op.alter_column('financial_asset_income', 'other_securities_net_income', existing_type=sa.Integer(), type_=sa.String(), server_default=' ') 

    op.execute(
        """
        ALTER TABLE financial_asset_income
        ALTER COLUMN other_securities_net_income DROP DEFAULT
        """
    )

    # Change column type of 'other_securities_net_income' back from Integer to String
    op.execute(
        """
        ALTER TABLE financial_asset_income
        ALTER COLUMN other_securities_net_income TYPE VARCHAR
        """
    )

    # Optionally, set the original default value back
    op.execute(
        """
        ALTER TABLE financial_asset_income
        ALTER COLUMN other_securities_net_income SET DEFAULT ''
        """
    )