"""add tax payer status column in tax table

Revision ID: 259432ae2ea7
Revises: 45da58e205fd
Create Date: 2024-12-03 17:14:27.030311

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '259432ae2ea7'
down_revision: Union[str, None] = '45da58e205fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('tax', sa.Column('min_tax', sa.Integer(), nullable=False, server_default='0'))


def downgrade() -> None:
    op.drop_column('tax', 'min_tax')