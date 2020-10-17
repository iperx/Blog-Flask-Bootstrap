"""empty message

Revision ID: c89d97582b37
Revises: 5f0b382402ea
Create Date: 2020-10-17 15:26:37.688477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c89d97582b37'
down_revision = '5f0b382402ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('author', sa.String(length=30), nullable=True))
    op.add_column('tag', sa.Column('author', sa.String(length=30), nullable=True))
    op.add_column('user', sa.Column('username', sa.String(length=30), nullable=True))
    op.create_unique_constraint(None, 'user', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'username')
    op.drop_column('tag', 'author')
    op.drop_column('post', 'author')
    # ### end Alembic commands ###