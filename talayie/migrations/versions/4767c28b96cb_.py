"""empty message

Revision ID: 4767c28b96cb
Revises: 
Create Date: 2023-06-22 18:21:21.140343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4767c28b96cb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('organizations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('foods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('is_available', sa.Boolean(), nullable=True),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('personnels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('date_of_birth', sa.String(length=128), nullable=True),
    sa.Column('role', sa.Integer(), nullable=True),
    sa.Column('organization', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['organization'], ['organizations.id'], ),
    sa.ForeignKeyConstraint(['role'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('clients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('personnel', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['personnel'], ['personnels.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_paid', sa.Boolean(), nullable=True),
    sa.Column('paid_date', sa.DateTime(), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('total_price', sa.Integer(), nullable=True),
    sa.Column('table_number', sa.Integer(), nullable=True),
    sa.Column('client', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['client'], ['clients.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orderitems',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('food_id', sa.Integer(), nullable=True),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['food_id'], ['foods.id'], name='fk_orderitem_food_id'),
    sa.ForeignKeyConstraint(['order'], ['orders.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orderitems')
    op.drop_table('orders')
    op.drop_table('clients')
    op.drop_table('personnels')
    op.drop_table('foods')
    op.drop_table('roles')
    op.drop_table('organizations')
    op.drop_table('categories')
    # ### end Alembic commands ###
