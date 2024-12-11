"""add income source area in taxpayer

Revision ID: 9eb06de82064
Revises: 94daddb4dc9e
Create Date: 2024-12-11 12:40:34.650446

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '9eb06de82064'
down_revision: Union[str, None] = '94daddb4dc9e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Create the Enum type in the database
    source_area_enum = sa.Enum('dhaka_chittagong', 'city', 'other', name='source_area')
    source_area_enum.create(op.get_bind())  # Explicitly create the Enum type

    # Add the 'source_area' column
    op.add_column('taxpayer', sa.Column('source_area', source_area_enum, nullable=True))
    
    # Create the index on 'source_area'
    op.create_index(op.f('ix_taxpayer_source_area'), 'taxpayer', ['source_area'], unique=False)


def downgrade() -> None:
    # Drop the index first
    op.drop_index(op.f('ix_taxpayer_source_area'), table_name='taxpayer')
    
    # Drop the 'source_area' column
    op.drop_column('taxpayer', 'source_area')
    
    # Remove the Enum type from the database
    source_area_enum = sa.Enum('dhaka_chittagong', 'city', 'other', name='source_area')
    source_area_enum.drop(op.get_bind())
