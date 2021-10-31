"""create_main_tables
Revision ID: 2085cef18a5d
Revises: 
Create Date: 2021-10-30 15:32:49.369119
"""

import os

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic
revision = '2085cef18a5d'
down_revision = None
branch_labels = None
depends_on = None
table_name = "coveragedb"


def create_table(table_name) -> None:
    op.create_table(
        table_name,
        sa.Column("Country", sa.Text, nullable=True),
        sa.Column("Region", sa.Text, nullable=True),
        sa.Column("Code", sa.Text, nullable=True),
        sa.Column("Date", sa.Text, nullable=True),
        sa.Column("Sex", sa.Text, nullable=True),
        sa.Column("Age", sa.Text, nullable=True),
        sa.Column("AgeInt", sa.Integer, nullable=True),
        sa.Column("Metric", sa.Text, nullable=True),
        sa.Column("Measure", sa.Text, nullable=True),
        sa.Column("Value", sa.Float, nullable=True),
        sa.Column("Short", sa.Text, nullable=True),
    )


def upgrade() -> None:
    create_table(table_name)


def downgrade() -> None:
    op.drop_table(table_name)
    pass
