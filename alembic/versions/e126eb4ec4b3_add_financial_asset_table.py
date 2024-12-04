"""add financial asset table

Revision ID: e126eb4ec4b3
Revises: 259432ae2ea7
Create Date: 2024-12-04 12:17:54.417510

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e126eb4ec4b3'
down_revision: Union[str, None] = '259432ae2ea7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'financial_asset_income',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('savings_ban_interest_net_income', sa.Integer(), server_default='0'),
        sa.Column('savings_ban_interest_tax_deduction_at_source', sa.Integer(), server_default='0'),
        sa.Column('savings_ban_interest_interest_on_loans', sa.Integer(), server_default='0'),
        sa.Column('savings_ban_interest_allowable_expenditure', sa.Integer(), server_default='0'),
        sa.Column('savings_ban_interest_taxable', sa.Integer(), server_default='0'),
        sa.Column('savings_ban_interest_description', sa.String(), server_default=''),
        sa.Column('other_securities_net_income', sa.String(), server_default=''),
        sa.Column('other_securities_tax_deduction_at_source', sa.Integer(), server_default='0'),
        sa.Column('other_securities_interest_on_loans', sa.Integer(), server_default='0'),
        sa.Column('other_securities_allowable_expenditure', sa.Integer(), server_default='0'),
        sa.Column('other_securities_taxable', sa.Integer(), server_default='0'),
        sa.Column('other_securities_description', sa.String(), server_default=''),
        sa.Column('income_from_islamic_principles_net_income', sa.Integer(), server_default='0'),
        sa.Column('income_from_islamic_principles_tax_deduction_at_source', sa.Integer(), server_default='0'),
        sa.Column('income_from_islamic_principles_interest_on_loans', sa.Integer(), server_default='0'),
        sa.Column('income_from_islamic_principles_allowable_expenditure', sa.Integer(), server_default='0'),
        sa.Column('income_from_islamic_principles_taxable', sa.Integer(), server_default='0'),
        sa.Column('income_from_islamic_principles_description', sa.String(), server_default=''),
        sa.Column('bank_interest_savings_deposits_net_income', sa.Integer(), server_default='0'),
        sa.Column('bank_interest_savings_deposits_tax_deduction_at_source', sa.Integer(), server_default='0'),
        sa.Column('bank_interest_savings_deposits_interest_on_loans', sa.Integer(), server_default='0'),
        sa.Column('bank_interest_savings_deposits_allowable_expenditure', sa.Integer(), server_default='0'),
        sa.Column('bank_interest_savings_deposits_taxable', sa.Integer(), server_default='0'),
        sa.Column('bank_interest_savings_deposits_description', sa.String(), server_default=''),
        sa.Column('fdr_interest_income_net_income', sa.Integer(), server_default='0'),
        sa.Column('fdr_interest_income_tax_deduction_at_source', sa.Integer(), server_default='0'),
        sa.Column('fdr_interest_income_interest_on_loans', sa.Integer(), server_default='0'),
        sa.Column('fdr_interest_income_allowable_expenditure', sa.Integer(), server_default='0'),
        sa.Column('fdr_interest_income_taxable', sa.Integer(), server_default='0'),
        sa.Column('fdr_interest_income_description', sa.String(), server_default=''),
        sa.Column('dividend_income_net_income', sa.Integer(), server_default='0'),
        sa.Column('dividend_income_tax_deduction_at_source', sa.Integer(), server_default='0'),
        sa.Column('dividend_income_interest_on_loans', sa.Integer(), server_default='0'),
        sa.Column('dividend_income_allowable_expenditure', sa.Integer(), server_default='0'),
        sa.Column('dividend_income_taxable', sa.Integer(), server_default='0'),
        sa.Column('dividend_income_description', sa.String(), server_default=''),
        sa.Column('reduced_tax_rate_securities_net_income', sa.Integer(), server_default='0'),
        sa.Column('reduced_tax_rate_securities_tax_deduction_at_source', sa.Integer(), server_default='0'),
        sa.Column('reduced_tax_rate_securities_interest_on_loans', sa.Integer(), server_default='0'),
        sa.Column('reduced_tax_rate_securities_allowable_expenditure', sa.Integer(), server_default='0'),
        sa.Column('reduced_tax_rate_securities_taxable', sa.Integer(), server_default='0'),
        sa.Column('reduced_tax_rate_securities_description', sa.String(), server_default=''),
        sa.Column('income_other_resources_net_income', sa.Integer(), server_default='0'),
        sa.Column('income_other_resources_tax_deduction_at_source', sa.Integer(), server_default='0'),
        sa.Column('income_other_resources_interest_on_loans', sa.Integer(), server_default='0'),
        sa.Column('income_other_resources_allowable_expenditure', sa.Integer(), server_default='0'),
        sa.Column('income_other_resources_taxable', sa.Integer(), server_default='0'),
        sa.Column('income_other_resources_description', sa.String(), server_default=''),
        sa.Column('us_dollar_investment_bonds_net_income', sa.Integer(), server_default='0'),
        sa.Column('us_dollar_investment_bonds_tax_deduction_at_source', sa.Integer(), server_default='0'),
        sa.Column('us_dollar_investment_bonds_interest_on_loans', sa.Integer(), server_default='0'),
        sa.Column('us_dollar_investment_bonds_allowable_expenditure', sa.Integer(), server_default='0'),
        sa.Column('us_dollar_investment_bonds_taxable', sa.Integer(), server_default='0'),
        sa.Column('us_dollar_investment_bonds_description', sa.String(), server_default=''),
        sa.Column('euro_premium_bonds_net_income', sa.Integer(), server_default='0'),
        sa.Column('euro_premium_bonds_tax_deduction_at_source', sa.Integer(), server_default='0'),
        sa.Column('euro_premium_bonds_interest_on_loans', sa.Integer(), server_default='0'),
        sa.Column('euro_premium_bonds_allowable_expenditure', sa.Integer(), server_default='0'),
        sa.Column('euro_premium_bonds_taxable', sa.Integer(), server_default='0'),
        sa.Column('euro_premium_bonds_description', sa.String(),   server_default=''),
        sa.Column('pound_sterling_premium_bonds_net_income', sa.Integer(), server_default='0'),
        sa.Column('pound_sterling_premium_bonds_tax_deduction_at_source', sa.Integer(), server_default='0'),
        sa.Column('pound_sterling_premium_bonds_interest_on_loans', sa.Integer(), server_default='0'),
        sa.Column('pound_sterling_premium_bonds_allowable_expenditure', sa.Integer(), server_default='0'),
        sa.Column('pound_sterling_premium_bonds_taxable', sa.Integer(), server_default='0'),
        sa.Column('pound_sterling_premium_bonds_description', sa.String(), server_default=''),
        sa.Column('us_dollar_premium_bonds_net_income', sa.Integer(), server_default='0'),
        sa.Column('us_dollar_premium_bonds_tax_deduction_at_source', sa.Integer(), server_default='0'),
        sa.Column('us_dollar_premium_bonds_interest_on_loans', sa.Integer(), server_default='0'),
        sa.Column('us_dollar_premium_bonds_allowable_expenditure', sa.Integer(), server_default='0'),
        sa.Column('us_dollar_premium_bonds_taxable', sa.Integer(), server_default='0'),
        sa.Column('us_dollar_premium_bonds_description', sa.String(), server_default=''),
        sa.Column('wage_earners_development_bonds_net_income', sa.Integer(), server_default='0'),
        sa.Column('wage_earners_development_bonds_tax_deduction_at_source', sa.Integer(), server_default='0'),
        sa.Column('wage_earners_development_bonds_interest_on_loans', sa.Integer(), server_default='0'),
        sa.Column('wage_earners_development_bonds_allowable_expenditure', sa.Integer(), server_default='0'),
        sa.Column('wage_earners_development_bonds_taxable', sa.Integer(), server_default='0'),
        sa.Column('wage_earners_development_bonds_description', sa.String(), server_default=''),
        sa.Column('euro_investment_bonds_net_income', sa.Integer(), server_default='0'),
        sa.Column('euro_investment_bonds_tax_deduction_at_source', sa.Integer(), server_default='0'),
        sa.Column('euro_investment_bonds_interest_on_loans', sa.Integer(), server_default='0'),
        sa.Column('euro_investment_bonds_allowable_expenditure', sa.Integer(), server_default='0'),
        sa.Column('euro_investment_bonds_taxable', sa.Integer(), server_default='0'),
        sa.Column('euro_investment_bonds_description', sa.String(), server_default=''),
        sa.Column('etin', sa.String(12), sa.ForeignKey('taxpayer.etin'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )



def downgrade() -> None:
    op.drop_table('financial_asset_income')
