<%!
from alembic.autogenerate import renderers
%>
"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from alembic import op
import sqlalchemy as sa

${imports if imports else ""}
def upgrade():
${upgrades | indent}

def downgrade():
${downgrades | indent}
