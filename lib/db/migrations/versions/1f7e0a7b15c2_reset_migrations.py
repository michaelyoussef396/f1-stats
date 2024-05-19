"""reset migrations

Revision ID: 1f7e0a7b15c2
Revises: 2330419002dd
Create Date: 2024-05-20 05:30:35.486842

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1f7e0a7b15c2'
down_revision = '2330419002dd'
branch_labels = None
depends_on = None


revision = '1f7e0a7b15c2'
down_revision = '2330419002dd'
branch_labels = None
depends_on = None


def upgrade():
    # Drop the unnamed foreign key constraint and the column
    with op.batch_alter_table('races', schema=None) as batch_op:
        batch_op.drop_column('circuitId')


def downgrade():
    # Add back the column and the foreign key constraint
    with op.batch_alter_table('races', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column('circuitId', sa.Integer(), nullable=False))
        # No name for the foreign key constraint
        batch_op.create_foreign_key(
            None, 'circuits', ['circuitId'], ['circuitId'])
