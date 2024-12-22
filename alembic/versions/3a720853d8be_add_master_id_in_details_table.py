"""add master id in details table

Revision ID: 3a720853d8be
Revises: 5ec29ca6d1dc
Create Date: 2024-12-22 12:56:20.742157

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '3a720853d8be'
down_revision: Union[str, None] = '5ec29ca6d1dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    
    op.add_column('rent_income_details', sa.Column('master_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'rent_income_details', 'rent_income_master', ['master_id'], ['id'])
    


def downgrade() -> None:
    
    op.drop_constraint(None, 'rent_income_details', type_='foreignkey')
    op.drop_column('rent_income_details', 'master_id')
   
