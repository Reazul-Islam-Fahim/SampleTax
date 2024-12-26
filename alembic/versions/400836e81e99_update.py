"""update

Revision ID: 400836e81e99
Revises: 3a720853d8be
Create Date: 2024-12-26 13:13:59.229364

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '400836e81e99'
down_revision: Union[str, None] = '3a720853d8be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass