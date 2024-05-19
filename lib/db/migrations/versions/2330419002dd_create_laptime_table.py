"""create laptime table

Revision ID: 2330419002dd
Revises: f146aba406fd
Create Date: 2024-05-20 05:23:43.385546

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2330419002dd'
down_revision: Union[str, None] = 'f146aba406fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('laptimes',
                    sa.Column('raceId', sa.Integer(), nullable=False),
                    sa.Column('driverId', sa.Integer(), nullable=False),
                    sa.Column('lap', sa.Integer(), nullable=False),
                    sa.Column('position', sa.Integer(), nullable=True),
                    sa.Column('time', sa.String(length=255), nullable=True),
                    sa.Column('milliseconds', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['driverId'], ['drivers.driverId'], ),
                    sa.ForeignKeyConstraint(['raceId'], ['races.raceId'], ),
                    sa.PrimaryKeyConstraint('raceId', 'driverId', 'lap')
                    )


def downgrade() -> None:
    op.drop_table('laptimes')
