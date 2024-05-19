"""create pitstop table

Revision ID: b9b5f9e11c61
Revises: af7ad1d3b309
Create Date: 2024-05-20 07:07:46.953491

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9b5f9e11c61'
down_revision: Union[str, None] = 'af7ad1d3b309'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Create a new table with the desired schema
    op.create_table('qualify_new',
                    sa.Column('qualifyId', sa.Integer(), nullable=False),
                    sa.Column('raceId', sa.Integer(), nullable=True),
                    sa.Column('driverId', sa.Integer(), nullable=True),
                    sa.Column('constructorId', sa.Integer(), nullable=True),
                    sa.Column('number', sa.Integer(), nullable=True),
                    sa.Column('position', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('qualifyId')
                    )

    # Copy data from the old table to the new table
    op.execute('INSERT INTO qualify_new SELECT * FROM qualify')

    # Drop the old table
    op.drop_table('qualify')

    # Rename the new table to 'qualify'
    op.rename_table('qualify_new', 'qualify')

    # Create the PitStop table
    op.create_table('pit_stops',
                    sa.Column('raceId', sa.Integer(), nullable=False),
                    sa.Column('driverId', sa.Integer(), nullable=False),
                    sa.Column('stop', sa.Integer(), nullable=False),
                    sa.Column('lap', sa.Integer(), nullable=True),
                    sa.Column('time', sa.Time(), nullable=True),
                    sa.Column('duration', sa.String(length=20), nullable=True),
                    sa.Column('milliseconds', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('raceId', 'driverId', 'stop')
                    )


def downgrade():
    # Drop the PitStop table
    op.drop_table('pit_stops')

    # Drop the new 'qualify' table
    op.drop_table('qualify')

    # Recreate the old 'qualify' table
    op.create_table('qualify',
                    sa.Column('qualifyId', sa.Integer(), nullable=False),
                    sa.Column('raceId', sa.Integer(), nullable=True),
                    sa.Column('driverId', sa.Integer(), nullable=True),
                    sa.Column('constructorId', sa.Integer(), nullable=True),
                    sa.Column('number', sa.Integer(), nullable=True),
                    sa.Column('position', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('qualifyId')
                    )
