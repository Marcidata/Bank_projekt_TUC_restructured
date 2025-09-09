"""migration customer example

Revision ID: mig_customer
Revises: ddf0b7aacda
Create Date: 2025-09-06 00:10:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = 'mig_customer'
down_revision = 'ddf0b7aacda'
branch_labels = None
depends_on = None

def upgrade():
    op.alter_column('customers', 'name', existing_type=sa.String(), nullable=False)

def downgrade():
    pass
