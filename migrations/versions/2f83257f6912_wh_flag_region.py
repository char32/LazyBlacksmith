"""wh_flag_region

Revision ID: 2f83257f6912
Revises: ce1e397f5ac
Create Date: 2015-11-20 15:17:57.565000

"""

# revision identifiers, used by Alembic.
revision = '2f83257f6912'
down_revision = 'ce1e397f5ac'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('region', sa.Column('wh', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('region', 'wh')
    ### end Alembic commands ###
