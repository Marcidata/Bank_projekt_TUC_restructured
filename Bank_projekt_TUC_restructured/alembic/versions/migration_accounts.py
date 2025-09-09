"""migration accounts example

Revision ID: mig_accounts
Revises: mig_customer
Create Date: 2025-09-06 00:15:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = 'mig_accounts'
down_revision = 'mig_customer'
branch_labels = None
depends_on = None

def upgrade():
    op.create_index('ix_accounts_account_number', 'accounts', ['account_number'])

def downgrade():
    op.drop_index('ix_accounts_account_number', table_name='accounts')
