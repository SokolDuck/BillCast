"""Create init tables

Revision ID: 609c730a5594
Revises: 7a781f90fc7d
Create Date: 2022-07-17 11:18:36.034450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '609c730a5594'
down_revision = '7a781f90fc7d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_shop_id'), 'shop', ['id'], unique=False)
    op.create_table('taxgroup',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('tax_value', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('tax_value')
    )
    op.create_index(op.f('ix_taxgroup_id'), 'taxgroup', ['id'], unique=False)
    op.create_table('unit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_unit_id'), 'unit', ['id'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_full_name'), 'user', ['full_name'], unique=False)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_full_name'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_unit_id'), table_name='unit')
    op.drop_table('unit')
    op.drop_index(op.f('ix_taxgroup_id'), table_name='taxgroup')
    op.drop_table('taxgroup')
    op.drop_index(op.f('ix_shop_id'), table_name='shop')
    op.drop_table('shop')
    # ### end Alembic commands ###
