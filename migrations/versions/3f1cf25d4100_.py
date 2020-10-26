"""empty message

Revision ID: 3f1cf25d4100
Revises: ae379df889e6
Create Date: 2020-10-26 17:16:04.295122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f1cf25d4100'
down_revision = 'ae379df889e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('items', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'items', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'items', type_='foreignkey')
    op.drop_column('items', 'user_id')
    op.drop_table('users')
    # ### end Alembic commands ###
