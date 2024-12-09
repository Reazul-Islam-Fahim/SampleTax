"""review all

Revision ID: 4fea00f14969
Revises: 
Create Date: 2024-12-09 15:49:53.371793

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4fea00f14969'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None






def upgrade() -> None:
    # Add the column as nullable initially
    op.add_column(
        'taxpayer',
        sa.Column('permanent_address', sa.String(length=500), nullable=True)
    )

    # Populate the column with default values
    op.execute("UPDATE taxpayer SET permanent_address = 'Not Provided' WHERE permanent_address IS NULL")

    # Alter the column to be NOT NULL
    op.alter_column('taxpayer', 'permanent_address', nullable=False)

    # Other upgrade operations
    op.alter_column('tax', 'min_tax',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.create_index(op.f('ix_tax_min_tax'), 'tax', ['min_tax'], unique=False)

    # Use explicit cast for ENUM change and handle default value explicitly
    op.execute("ALTER TABLE taxpayer ALTER COLUMN tax_payer_status DROP DEFAULT")
    op.execute("ALTER TABLE taxpayer ALTER COLUMN tax_payer_status TYPE taxpayerstatus USING tax_payer_status::text::taxpayerstatus")
    op.execute("ALTER TABLE taxpayer ALTER COLUMN tax_payer_status SET DEFAULT 'individual'")

    # Use explicit cast for marital_status ENUM change
    op.execute("ALTER TABLE taxpayer ALTER COLUMN marital_status DROP DEFAULT")
    op.execute("ALTER TABLE taxpayer ALTER COLUMN marital_status TYPE maritalstatus USING marital_status::text::maritalstatus")
    op.execute("ALTER TABLE taxpayer ALTER COLUMN marital_status SET DEFAULT 'unmarried'")

    op.alter_column('taxpayer', 'father_name',
               existing_type=sa.VARCHAR(length=100),
               nullable=False,
               existing_server_default=sa.text("' '::character varying"))
    op.alter_column('taxpayer', 'present_address',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=500),
               nullable=False,
               existing_server_default=sa.text("' '::character varying"))
    op.drop_index('ix_taxpayer_address', table_name='taxpayer')
    op.create_index(op.f('ix_taxpayer_father_name'), 'taxpayer', ['father_name'])
    op.create_index(op.f('ix_taxpayer_marital_status'), 'taxpayer', ['marital_status'])
    op.create_index(op.f('ix_taxpayer_permanent_address'), 'taxpayer', ['permanent_address'])
    op.create_index(op.f('ix_taxpayer_present_address'), 'taxpayer', ['present_address'])
    op.create_index(op.f('ix_taxpayer_tax_payer_status'), 'taxpayer', ['tax_payer_status'])
    op.drop_column('taxpayer', 'permanant_address')

def downgrade() -> None:
    # Revert changes in downgrade
    op.add_column('taxpayer', sa.Column('permanant_address', sa.VARCHAR(length=500), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_taxpayer_tax_payer_status'), table_name='taxpayer')
    op.drop_index(op.f('ix_taxpayer_present_address'), table_name='taxpayer')
    op.drop_index(op.f('ix_taxpayer_permanent_address'), table_name='taxpayer')
    op.drop_index(op.f('ix_taxpayer_marital_status'), table_name='taxpayer')
    op.drop_index(op.f('ix_taxpayer_father_name'), table_name='taxpayer')
    op.create_index('ix_taxpayer_address', 'taxpayer', ['permanant_address'], unique=False)
    op.alter_column('taxpayer', 'present_address',
               existing_type=sa.String(length=500),
               type_=sa.VARCHAR(length=100),
               nullable=True,
               existing_server_default=sa.text("' '::character varying"))
    op.execute("ALTER TABLE taxpayer ALTER COLUMN marital_status DROP DEFAULT")
    op.execute("ALTER TABLE taxpayer ALTER COLUMN marital_status TYPE VARCHAR")
    op.execute("ALTER TABLE taxpayer ALTER COLUMN marital_status SET DEFAULT 'unmarried'")
    op.alter_column('taxpayer', 'father_name',
               existing_type=sa.VARCHAR(length=100),
               nullable=True,
               existing_server_default=sa.text("' '::character varying"))
    op.execute("ALTER TABLE taxpayer ALTER COLUMN tax_payer_status DROP DEFAULT")
    op.execute("ALTER TABLE taxpayer ALTER COLUMN tax_payer_status TYPE VARCHAR")
    op.execute("ALTER TABLE taxpayer ALTER COLUMN tax_payer_status SET DEFAULT 'individual'")
    op.drop_column('taxpayer', 'permanent_address')
    op.drop_index(op.f('ix_tax_min_tax'), table_name='tax')
    op.alter_column('tax', 'min_tax',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text('0'))
