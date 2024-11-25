"""create test table

Revision ID: fea44fd3e44c
Revises: e1279b10a740
Create Date: 2024-11-24 15:19:17.508969

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fea44fd3e44c'
down_revision: Union[str, None] = 'e1279b10a740'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )

def downgrade() -> None:
    op.drop_table('account')
