"""added is_paid to basket

Revision ID: 99df8548352b
Revises: 4dba94b324b3
Create Date: 2020-01-27 18:22:35.710495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99df8548352b'
down_revision = '4dba94b324b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('basket', sa.Column('is_paid', sa.Boolean(), nullable=True))
    op.drop_column('stores_products', 'is_paid')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stores_products', sa.Column('is_paid', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('basket', 'is_paid')
    # ### end Alembic commands ###