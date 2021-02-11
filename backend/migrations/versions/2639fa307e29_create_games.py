"""create games

Revision ID: 2639fa307e29
Revises:
Create Date: 2021-02-09 20:54:46.904216

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2639fa307e29'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('publisher_website', sa.String(length=255), nullable=True),
    sa.Column('logo_img_src', sa.String(length=255), nullable=True),
    sa.Column('logo_img_alt', sa.String(length=255), nullable=True),
    sa.Column('logo_img_style', sa.JSON(), nullable=True),
    sa.Column('tagline', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('games')
    # ### end Alembic commands ###
