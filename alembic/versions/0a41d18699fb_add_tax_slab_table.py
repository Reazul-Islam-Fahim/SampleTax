"""add tax slab table

Revision ID: 0a41d18699fb
Revises: 4fea00f14969
Create Date: 2024-12-09 16:48:52.438080

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '0a41d18699fb'
down_revision: Union[str, None] = '4fea00f14969'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('tax_slab', sa.Column('second', sa.Integer(), nullable=True))
    op.add_column('tax_slab', sa.Column('third', sa.Integer(), nullable=True))
    op.add_column('tax_slab', sa.Column('fourth', sa.Integer(), nullable=True))
    op.add_column('tax_slab', sa.Column('fifth', sa.Integer(), nullable=True))
    op.add_column('tax_slab', sa.Column('sixth', sa.Integer(), nullable=True))
    op.add_column('tax_slab', sa.Column('seventh', sa.Integer(), nullable=True))
    op.add_column('tax_slab', sa.Column('etin', sa.String(length=12), nullable=False))
    op.create_foreign_key(None, 'tax_slab', 'taxpayer', ['etin'], ['etin'])
    
    


def downgrade() -> None:
    
    op.drop_constraint(None, 'tax_slab', type_='foreignkey')
    op.drop_column('tax_slab', 'etin')
    op.drop_column('tax_slab', 'seventh')
    op.drop_column('tax_slab', 'sixth')
    op.drop_column('tax_slab', 'fifth')
    op.drop_column('tax_slab', 'fourth')
    op.drop_column('tax_slab', 'third')
    op.drop_column('tax_slab', 'second')
    
