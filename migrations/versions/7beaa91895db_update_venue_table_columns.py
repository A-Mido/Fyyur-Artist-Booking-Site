"""update  venue table columns.

Revision ID: 7beaa91895db
Revises: 0c49a0723a88
Create Date: 2020-10-18 19:31:09.262710

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7beaa91895db'
down_revision = '0c49a0723a88'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('venue', 'address',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('venue', 'city',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('venue', 'state',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('venue', 'state',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('venue', 'city',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('venue', 'address',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    # ### end Alembic commands ###
