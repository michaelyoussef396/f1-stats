"""create races table with foreign key constrain

Revision ID: f8dcd4a8c48a
Revises: 8dc0e79f3ddc
Create Date: 2024-05-20 06:15:23.885586

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f8dcd4a8c48a'
down_revision: Union[str, None] = '8dc0e79f3ddc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table('races')
    op.create_table('races',
                    sa.Column('raceId', sa.Integer(), nullable=False),
                    sa.Column('year', sa.Integer(), nullable=False),
                    sa.Column('round', sa.Integer(), nullable=False),
                    sa.Column('circuitId', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=255), nullable=False),
                    sa.Column('date', sa.Date(), nullable=False),
                    sa.Column('time', sa.Time(), nullable=True),
                    sa.Column('url', sa.String(length=255), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['circuitId'], ['circuits.circuitId'], ),
                    sa.PrimaryKeyConstraint('raceId')
                    )


def downgrade() -> None:
    op.drop_table('races')
