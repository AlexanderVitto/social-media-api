"""add content column to posts table

Revision ID: 83fc67dafa8c
Revises: b939d1c14089
Create Date: 2024-01-29 10:51:53.165960

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '83fc67dafa8c'
down_revision: Union[str, None] = 'b939d1c14089'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
