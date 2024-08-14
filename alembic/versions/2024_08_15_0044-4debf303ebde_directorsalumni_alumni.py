"""DirectorsAlumni+Alumni

Revision ID: 4debf303ebde
Revises: 68ca4dd3633b
Create Date: 2024-08-15 00:44:00.333449

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4debf303ebde"
down_revision: Union[str, None] = "68ca4dd3633b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "alumni",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.Column("contact_info", sa.String(), nullable=False),
        sa.Column("work_location", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_alumni")),
    )
    op.create_index(
        op.f("ix_alumni_first_name"), "alumni", ["first_name"], unique=False
    )
    op.create_index(
        op.f("ix_alumni_last_name"), "alumni", ["last_name"], unique=False
    )
    op.create_table(
        "directors_alumni",
        sa.Column("director_id", sa.Integer(), nullable=False),
        sa.Column("alumni_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["alumni_id"],
            ["alumni.id"],
            name=op.f("fk_directors_alumni_alumni_id_alumni"),
        ),
        sa.ForeignKeyConstraint(
            ["director_id"],
            ["directors.id"],
            name=op.f("fk_directors_alumni_director_id_directors"),
        ),
        sa.PrimaryKeyConstraint(
            "director_id", "alumni_id", name=op.f("pk_directors_alumni")
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    op.drop_table("directors_alumni")
    op.drop_index(op.f("ix_alumni_last_name"), table_name="alumni")
    op.drop_index(op.f("ix_alumni_first_name"), table_name="alumni")
    op.drop_table("alumni")
    # ### end Alembic commands ###
