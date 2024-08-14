"""Programs+States+Directors+Statistics

Revision ID: 400397bb2cc3
Revises: 
Create Date: 2024-08-15 00:02:56.083071

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "400397bb2cc3"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "directors",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.Column("contact_info", sa.String(), nullable=False),
        sa.Column("specialty", sa.String(), nullable=True),
        sa.Column("home_country", sa.String(), nullable=True),
        sa.Column("additional_info", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_directors")),
    )
    op.create_index(
        op.f("ix_directors_first_name"),
        "directors",
        ["first_name"],
        unique=False,
    )
    op.create_index(
        op.f("ix_directors_last_name"),
        "directors",
        ["last_name"],
        unique=False,
    )
    op.create_table(
        "states",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("region", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_states")),
    )
    op.create_index(op.f("ix_states_title"), "states", ["title"], unique=False)
    op.create_table(
        "programs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("code", sa.String(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("city", sa.String(), nullable=False),
        sa.Column("state_id", sa.Integer(), nullable=False),
        sa.Column("director_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["director_id"],
            ["directors.id"],
            name=op.f("fk_programs_director_id_directors"),
        ),
        sa.ForeignKeyConstraint(
            ["state_id"],
            ["states.id"],
            name=op.f("fk_programs_state_id_states"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_programs")),
    )
    op.create_index(
        op.f("ix_programs_code"), "programs", ["code"], unique=True
    )
    op.create_index(
        op.f("ix_programs_director_id"),
        "programs",
        ["director_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_programs_state_id"), "programs", ["state_id"], unique=False
    )
    op.create_table(
        "program_statistics",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("percentage_non_us_img", sa.Numeric(), nullable=False),
        sa.Column(
            "percentage_applicants_interviewed", sa.Numeric(), nullable=True
        ),
        sa.Column("internship_available", sa.Boolean(), nullable=True),
        sa.Column(
            "more_than_two_russians_interviewed", sa.Boolean(), nullable=True
        ),
        sa.Column(
            "predominant_further_track",
            sa.ARRAY(
                sa.Enum(
                    "academic",
                    "full-time",
                    "residency",
                    "other",
                    name="further_track_enum",
                )
            ),
            nullable=True,
        ),
        sa.Column("additional_info", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["id"],
            ["programs.id"],
            name=op.f("fk_program_statistics_id_programs"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_program_statistics")),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    op.drop_table("program_statistics")
    op.drop_index(op.f("ix_programs_state_id"), table_name="programs")
    op.drop_index(op.f("ix_programs_director_id"), table_name="programs")
    op.drop_index(op.f("ix_programs_code"), table_name="programs")
    op.drop_table("programs")
    op.drop_index(op.f("ix_states_title"), table_name="states")
    op.drop_table("states")
    op.drop_index(op.f("ix_directors_last_name"), table_name="directors")
    op.drop_index(op.f("ix_directors_first_name"), table_name="directors")
    op.drop_table("directors")
    # ### end Alembic commands ###
