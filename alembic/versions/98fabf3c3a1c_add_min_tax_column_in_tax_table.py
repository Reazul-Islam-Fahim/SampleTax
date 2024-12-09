"""add min_tax column in tax table

Revision ID: 98fabf3c3a1c
Revises: c40fae7953cd
Create Date: 2024-12-09 11:14:10.135228

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98fabf3c3a1c'
down_revision: Union[str, None] = 'c40fae7953cd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('tax', sa.Column('min_tax', sa.Integer(), server_default='0'))
    # op.create_index(op.f('ix_tax_min_tax'), 'tax', ['min_tax'], unique=False)
    


def downgrade() -> None:
    # op.drop_index(op.f('ix_tax_min_tax'), table_name='tax')
    op.drop_column('tax', 'min_tax')
