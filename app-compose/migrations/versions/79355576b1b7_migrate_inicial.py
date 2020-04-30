"""Migrate inicial

Revision ID: 79355576b1b7
Revises: 
Create Date: 2020-04-30 00:39:49.036363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79355576b1b7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aluno',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=255), nullable=False),
    sa.Column('sobrenome', sa.String(length=255), nullable=False),
    sa.Column('idade', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('aluno')
    # ### end Alembic commands ###