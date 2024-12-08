"""rename column in taxpayer

Revision ID: 96dff94a23c6
Revises: 
Create Date: 2024-12-08 12:53:39.321579

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '96dff94a23c6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Create the 'taxpayerstatus' and 'maritalstatus' enum types
    op.execute(
        "CREATE TYPE taxpayerstatus AS ENUM ('individual', 'firm', 'hindu', 'other')"
    )
    op.execute(
        "CREATE TYPE maritalstatus AS ENUM ('married', 'unmarried')"
    )

    # Add new columns to 'taxpayer'
    op.add_column(
        'taxpayer',
        sa.Column(
            'tax_payer_status',
            sa.Enum('individual', 'firm', 'hindu', 'other', name='taxpayerstatus'),
            server_default='individual',
            nullable=False
        )
    )
    op.add_column(
        'taxpayer',
        sa.Column('father_name', sa.String(length=100), nullable=False, server_default=" ")
    )
    op.add_column(
        'taxpayer',
        sa.Column(
            'marital_status',
            sa.Enum('married', 'unmarried', name='maritalstatus'),
            server_default='unmarried',
            nullable=False
        )
    )
    op.add_column(
        'taxpayer',
        sa.Column(
            'permanent_address',
            sa.String(length=500),
            server_default=" ",
            nullable=True
        )
    )
    op.add_column(
        'taxpayer',
        sa.Column(
            'present_address',
            sa.String(length=500),
            server_default=" ",
            nullable=True
        )
    )

    # Drop the existing index on 'address' and remove the 'address' column
    op.drop_index('ix_taxpayer_address', table_name='taxpayer')
    op.drop_column('taxpayer', 'address')

    # Create new indexes
    op.create_index(op.f('ix_taxpayer_father_name'), 'taxpayer', ['father_name'], unique=False)
    op.create_index(op.f('ix_taxpayer_marital_status'), 'taxpayer', ['marital_status'], unique=False)
    op.create_index(op.f('ix_taxpayer_permanent_address'), 'taxpayer', ['permanent_address'], unique=False)
    op.create_index(op.f('ix_taxpayer_present_address'), 'taxpayer', ['present_address'], unique=False)
    op.create_index(op.f('ix_taxpayer_tax_payer_status'), 'taxpayer', ['tax_payer_status'], unique=False)


def downgrade():
    # Drop the new columns added in the upgrade
    op.drop_column('taxpayer', 'tax_payer_status')
    op.drop_column('taxpayer', 'father_name')
    op.drop_column('taxpayer', 'marital_status')
    op.drop_column('taxpayer', 'permanent_address')
    op.drop_column('taxpayer', 'present_address')

    # Drop the newly created indexes
    op.drop_index(op.f('ix_taxpayer_father_name'), table_name='taxpayer')
    op.drop_index(op.f('ix_taxpayer_marital_status'), table_name='taxpayer')
    op.drop_index(op.f('ix_taxpayer_permanent_address'), table_name='taxpayer')
    op.drop_index(op.f('ix_taxpayer_present_address'), table_name='taxpayer')
    op.drop_index(op.f('ix_taxpayer_tax_payer_status'), table_name='taxpayer')

    # Add back the 'address' column and its index
    op.add_column(
        'taxpayer',
        sa.Column('address', sa.String(length=255), nullable=True)
    )
    op.create_index('ix_taxpayer_address', 'taxpayer', ['address'], unique=False)

    # Drop the Enum types
    op.execute("DROP TYPE IF EXISTS taxpayerstatus")
    op.execute("DROP TYPE IF EXISTS maritalstatus")