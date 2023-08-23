"""add is_active to services

Revision ID: 503518b3d382
Revises: b4abeac4d60f
Create Date: 2023-08-23 12:16:38.989939

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '503518b3d382'
down_revision: Union[str, None] = 'b4abeac4d60f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
