"""initial tables

Revision ID: 8235370c22e9
Revises: 
Create Date: 2025-09-06 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = '8235370c22e9'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('customers',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('address', sa.String()),
        sa.Column('phone', sa.String()),
        sa.Column('national_id', sa.String(), unique=True)
    )
    op.create_table('accounts',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('account_number', sa.String(), unique=True, nullable=False),
        sa.Column('customer_id', sa.Integer(), sa.ForeignKey('customers.id')),
        sa.Column('balance', sa.Numeric(), server_default='0')
    )
    op.create_table('transactions',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('tx_id', sa.String(), unique=True, nullable=False),
        sa.Column('from_account', sa.String()),
        sa.Column('to_account', sa.String()),
        sa.Column('amount', sa.Numeric(), nullable=False),
        sa.Column('currency', sa.String(), server_default='SEK'),
        sa.Column('timestamp', sa.DateTime()),
        sa.Column('is_incoming', sa.Boolean(), server_default='true'),
        sa.Column('validated', sa.Boolean(), server_default='false'),
        sa.Column('suspicious', sa.Boolean(), server_default='false')
    )

def downgrade():
    op.drop_table('transactions')
    op.drop_table('accounts')
    op.drop_table('customers')
