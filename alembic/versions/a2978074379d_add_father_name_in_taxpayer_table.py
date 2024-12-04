"""add father name in taxpayer table

Revision ID: a2978074379d
Revises: e126eb4ec4b3
Create Date: 2024-12-04 12:54:59.055500

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a2978074379d'
down_revision: Union[str, None] = 'e126eb4ec4b3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('taxpayer', sa.Column('father_name', sa.String(length=100), server_default=' '))


def downgrade():
    op.drop_column('taxpayer', 'father_name')