"""Fix ProgramStatistics model

Revision ID: 160c86425c69
Revises: 4debf303ebde
Create Date: 2024-08-15 14:54:38.063501

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "160c86425c69"
down_revision: Union[str, None] = "4debf303ebde"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "program_statistics",
        "additional_info",
        existing_type=sa.VARCHAR(),
        nullable=True,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    op.alter_column(
        "program_statistics",
        "additional_info",
        existing_type=sa.VARCHAR(),
        nullable=False,
    )
    # ### end Alembic commands ###
