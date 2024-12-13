"""empty message

Revision ID: 098faa776f24
Revises: a65b79756f95
Create Date: 2024-12-13 12:24:46.817010

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '098faa776f24'
down_revision: Union[str, None] = 'a65b79756f95'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
    INSERT INTO tasks(name) VALUES
    ('test1'),
    ('test2'),
    ('test3')
    """)
    

def downgrade() -> None:
    op.execute("""
    DELETE FROM tasks
    WHERE name LIKE 'test%'
    """)

