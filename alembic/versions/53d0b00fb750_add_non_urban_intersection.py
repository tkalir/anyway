"""add non_urban_intersection

Revision ID: 53d0b00fb750
Revises: 11ddb0cff075
Create Date: 2024-06-16 15:05:30.522542

"""

# revision identifiers, used by Alembic.
revision = '53d0b00fb750'
down_revision = '11ddb0cff075'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('involved_markers_hebrew', sa.Column('urban_intersection', sa.Integer(), nullable=True))
    op.add_column('vehicles_markers_hebrew', sa.Column('urban_intersection', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vehicles_markers_hebrew', 'urban_intersection')
    op.drop_column('involved_markers_hebrew', 'urban_intersection')
    # ### end Alembic commands ###
