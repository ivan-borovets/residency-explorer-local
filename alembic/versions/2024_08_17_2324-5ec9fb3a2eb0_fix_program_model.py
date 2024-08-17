"""Fix Program model

Revision ID: 5ec9fb3a2eb0
Revises: 6bf2810bcca8
Create Date: 2024-08-17 23:24:18.328283

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5ec9fb3a2eb0"
down_revision: Union[str, None] = "6bf2810bcca8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "programs", sa.Column("user_rating", sa.Integer(), nullable=True)
    )
    op.drop_column("programs", "custom_rating")
    # ### end Alembic commands ###


def downgrade() -> None:
    op.add_column(
        "programs",
        sa.Column(
            "custom_rating", sa.INTEGER(), autoincrement=False, nullable=True
        ),
    )
    op.drop_column("programs", "user_rating")
    # ### end Alembic commands ###
