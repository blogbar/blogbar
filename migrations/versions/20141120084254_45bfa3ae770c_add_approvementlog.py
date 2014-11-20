"""Add ApprovementLog.

Revision ID: 45bfa3ae770c
Revises: 23e406f6c81b
Create Date: 2014-11-20 08:42:54.418285

"""

# revision identifiers, used by Alembic.
revision = '45bfa3ae770c'
down_revision = '23e406f6c81b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('approvement_log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('approved_at', sa.DateTime(), nullable=True),
    sa.Column('message', sa.Text(), nullable=True),
    sa.Column('blog_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blog_id'], ['blog.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('approvement_log')
    ### end Alembic commands ###