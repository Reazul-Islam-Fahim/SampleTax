"""add tax payer status column in taxpayer table

Revision ID: 45da58e205fd
Revises: 
Create Date: 2024-12-03 12:39:35.620478

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '45da58e205fd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('taxpayer', sa.Column('tax_payer_status', sa.String(), nullable=False, server_default='individual'))


def downgrade() -> None:
    op.drop_column('taxpayer', 'tax_payer_status')
