"""empty message

Revision ID: 44552e9fdead
Revises: 6e78226005e6
Create Date: 2016-10-05 02:02:17.183163

"""

# revision identifiers, used by Alembic.
revision = '44552e9fdead'
down_revision = '6e78226005e6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(), nullable=False))
    op.alter_column('user', 'geb',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('user', 'nachname',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)
    op.alter_column('user', 'vorname',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)
    op.create_unique_constraint(None, 'user', ['username'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.alter_column('user', 'vorname',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
    op.alter_column('user', 'nachname',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
    op.alter_column('user', 'geb',
               existing_type=sa.DATE(),
               nullable=True)
    op.drop_column('user', 'username')
    ### end Alembic commands ###
