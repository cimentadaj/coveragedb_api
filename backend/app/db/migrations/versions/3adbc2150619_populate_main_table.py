"""populate_main_table
Revision ID: 3adbc2150619
Revises: 2085cef18a5d
Create Date: 2021-10-30 16:49:10.949972
"""

import os

# import pandas as pd
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic
revision = '3adbc2150619'
down_revision = '2085cef18a5d'
branch_labels = None
depends_on = None
table_name = "coveragedb"


def copy_raw_data(table_name) -> None:
    # This is the path INSIDE the postgres container. Note that we link our local inputDB
    # to the postgres container in docker-compose.
    file_name = "/input_data/inputDB.utf8.csv"
    op.execute(
        f"copy {table_name} from '{file_name}' delimiter ',' csv header;",
        execution_options=None)


def upgrade() -> None:
    copy_raw_data(table_name)


def downgrade() -> None:
    pass
