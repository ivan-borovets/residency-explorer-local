"""Fix Program model

Revision ID: 95e68c5184c5
Revises: 160c86425c69
Create Date: 2024-08-15 15:16:05.131422

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "95e68c5184c5"
down_revision: Union[str, None] = "160c86425c69"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "programs", sa.Column("custom_rating", sa.Integer(), nullable=True)
    )
    # a line below is added manually
    op.create_check_constraint(
        constraint_name="check_custom_rating",
        table_name="programs",
        condition="custom_rating IS NULL OR (custom_rating >= 1 AND custom_rating <= 10)"
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # a line below is added manually
    op.drop_constraint("check_custom_rating", "programs", type_="check")
    op.drop_column("programs", "custom_rating")
    # ### end Alembic commands ###
