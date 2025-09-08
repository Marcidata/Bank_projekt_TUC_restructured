"""migration transactions example

Revision ID: mig_transactions
Revises: mig_accounts
Create Date: 2025-09-06 00:20:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = 'mig_transactions'
down_revision = 'mig_accounts'
branch_labels = None
depends_on = None

def upgrade():
    # exempel: lägg till kolumn för fee
    op.add_column('transactions', sa.Column('fee', sa.Numeric(), server_default='0'))

def downgrade():
    op.drop_column('transactions', 'fee')
