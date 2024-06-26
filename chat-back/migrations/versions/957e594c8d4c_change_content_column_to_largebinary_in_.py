"""Change content column to LargeBinary in Poste

Revision ID: 957e594c8d4c
Revises: bce597710008
Create Date: 2024-06-25 23:06:10.354993

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '957e594c8d4c'
down_revision = 'bce597710008'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('poste', schema=None) as batch_op:
        batch_op.alter_column('content',
               existing_type=mysql.TEXT(),
               type_=sa.LargeBinary(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('poste', schema=None) as batch_op:
        batch_op.alter_column('content',
               existing_type=sa.LargeBinary(),
               type_=mysql.TEXT(),
               existing_nullable=False)

    # ### end Alembic commands ###
