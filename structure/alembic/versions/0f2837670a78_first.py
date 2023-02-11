"""first

Revision ID: 0f2837670a78
Revises: 
Create Date: 2023-02-11 18:47:33.483020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f2837670a78'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'movies2',
        sa.Column('title2', sa.String(50), primary_key=True),
        sa.Column('genero2', sa.String(50), nullable=False),
        sa.Column('year2', sa.Integer, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('movies2')
