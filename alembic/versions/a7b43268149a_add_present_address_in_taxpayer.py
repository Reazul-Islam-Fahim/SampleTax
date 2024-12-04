"""add present address in taxpayer

Revision ID: a7b43268149a
Revises: 2aa8ccad8f95
Create Date: 2024-12-04 15:48:07.010501

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a7b43268149a'
down_revision: Union[str, None] = '2aa8ccad8f95'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('taxpayer', sa.Column('present_address', sa.String(length=100), server_default=' '))
    op.add_column('taxpayer', sa.Column('marital_status', sa.String(length=100), server_default='unmarried'))


def downgrade():
    op.drop_column('taxpayer', 'present_address')
    op.drop_column('taxpayer', 'marital_status')