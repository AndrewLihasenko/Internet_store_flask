"""

Revision ID: cb8e09274f14
Revises: ab2f7a2ae006
Create Date: 2020-02-05 18:21:04.807179

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb8e09274f14'
down_revision = 'ab2f7a2ae006'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order_product', sa.Column('product_id', sa.Integer(), nullable=False))
    op.add_column('order_product', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'order_product', 'users_table', ['user_id'], ['id'])
    op.create_foreign_key(None, 'order_product', 'products_table', ['product_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'order_product', type_='foreignkey')
    op.drop_constraint(None, 'order_product', type_='foreignkey')
    op.drop_column('order_product', 'user_id')
    op.drop_column('order_product', 'product_id')
    # ### end Alembic commands ###
