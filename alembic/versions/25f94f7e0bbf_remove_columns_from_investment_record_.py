"""Remove columns from investment_record table

Revision ID: 25f94f7e0bbf
Revises: 
Create Date: 2024-12-01 16:17:21.024933

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '25f94f7e0bbf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Remove columns from the investment_record table
    op.drop_column('investment_record', 'premium_or_contractual_deferred_annuity_actual')
    op.drop_column('investment_record', 'premium_or_contractual_deferred_annuity_allowable')
    op.drop_column('investment_record', 'premium_or_contractual_deferred_annuity_remarks')


def downgrade() -> None:
    # Recreate columns in case of rollback
    op.add_column('investment_record', sa.Column('premium_or_contractual_deferred_annuity_actual', sa.Integer(), server_default='0', nullable=False))
    op.add_column('investment_record', sa.Column('premium_or_contractual_deferred_annuity_allowable', sa.Integer(), server_default='0', nullable=False))
    op.add_column('investment_record', sa.Column('premium_or_contractual_deferred_annuity_remarks', sa.String(), nullable=True))
