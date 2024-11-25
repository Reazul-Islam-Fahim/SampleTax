"""Add a column

Revision ID: 52a36cd215d2
Revises: fea44fd3e44c
Create Date: 2024-11-24 15:33:24.201064

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '52a36cd215d2'
down_revision: Union[str, None] = 'fea44fd3e44c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))


def downgrade() -> None:
    op.drop_column('account', 'last_transaction_date')

