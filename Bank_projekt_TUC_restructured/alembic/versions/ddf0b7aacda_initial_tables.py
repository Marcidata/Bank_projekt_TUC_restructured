"""additional initial - exempel

Revision ID: ddf0b7aacda
Revises: 8235370c22e9
Create Date: 2025-09-06 00:05:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = 'ddf0b7aacda'
down_revision = '8235370c22e9'
branch_labels = None
depends_on = None

def upgrade():
    # exempel: lägg till kolumn i accounts
    op.add_column('accounts', sa.Column('account_type', sa.String(), server_default='standard'))

def downgrade():
    op.drop_column('accounts', 'account_type')
