"""add exampted amount fields in financial asset table

Revision ID: 2aa8ccad8f95
Revises: a2978074379d
Create Date: 2024-12-04 14:57:44.589235

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2aa8ccad8f95'
down_revision: Union[str, None] = 'a2978074379d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('financial_asset_income', sa.Column('us_dollar_investment_bonds_exampted_amount', sa.Integer(), server_default='0'))
    op.add_column('financial_asset_income', sa.Column('euro_premium_bonds_exampted_amount', sa.Integer(), server_default='0'))
    op.add_column('financial_asset_income', sa.Column('pound_sterling_premium_bonds_exampted_amount', sa.Integer(), server_default='0'))
    op.add_column('financial_asset_income', sa.Column('us_dollar_premium_bonds_exampted_amount', sa.Integer(), server_default='0'))
    op.add_column('financial_asset_income', sa.Column('wage_earners_development_bonds_exampted_amount', sa.Integer(), server_default='0'))
    op.add_column('financial_asset_income', sa.Column('euro_investment_bonds_exampted_amount', sa.Integer(), server_default='0'))


def downgrade() -> None:
    op.drop_column('financial_asset_income', 'us_dollar_investment_bonds_exampted_amount')
    op.drop_column('financial_asset_income', 'euro_premium_bonds_exampted_amount')
    op.drop_column('financial_asset_income', 'pound_sterling_premium_bonds_exampted_amount')
    op.drop_column('financial_asset_income', 'us_dollar_premium_bonds_exampted_amount')
    op.drop_column('financial_asset_income', 'wage_earners_development_bonds_exampted_amount')
    op.drop_column('financial_asset_income', 'euro_investment_bonds_exampted_amount')