"""All 8 models

Revision ID: aa3965303272
Revises: 
Create Date: 2024-08-15 21:31:57.932471

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "aa3965303272"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "alumni",
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.Column("contact_info", sa.String(), nullable=False),
        sa.Column("work_location", sa.String(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_alumni")),
    )
    op.create_index(
        op.f("ix_alumni_first_name"), "alumni", ["first_name"], unique=False
    )
    op.create_index(
        op.f("ix_alumni_last_name"), "alumni", ["last_name"], unique=False
    )
    op.create_table(
        "directors",
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.Column("contact_info", sa.String(), nullable=False),
        sa.Column("specialty", sa.String(), nullable=True),
        sa.Column("home_country", sa.String(), nullable=True),
        sa.Column("additional_info", sa.String(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
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
        "peers",
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.Column("contact_info", sa.String(), nullable=False),
        sa.Column("position", sa.String(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_peers")),
    )
    op.create_index(
        op.f("ix_peers_first_name"), "peers", ["first_name"], unique=False
    )
    op.create_index(
        op.f("ix_peers_last_name"), "peers", ["last_name"], unique=False
    )
    op.create_table(
        "states",
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("region", sa.String(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_states")),
    )
    op.create_index(op.f("ix_states_title"), "states", ["title"], unique=False)
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
    op.create_table(
        "directors_peers",
        sa.Column("director_id", sa.Integer(), nullable=False),
        sa.Column("peer_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["director_id"],
            ["directors.id"],
            name=op.f("fk_directors_peers_director_id_directors"),
        ),
        sa.ForeignKeyConstraint(
            ["peer_id"],
            ["peers.id"],
            name=op.f("fk_directors_peers_peer_id_peers"),
        ),
        sa.PrimaryKeyConstraint(
            "director_id", "peer_id", name=op.f("pk_directors_peers")
        ),
    )
    op.create_table(
        "programs",
        sa.Column("code", sa.String(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("city", sa.String(), nullable=False),
        sa.Column("custom_rating", sa.Integer(), nullable=True),
        sa.Column("state_id", sa.Integer(), nullable=False),
        sa.Column("director_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.CheckConstraint(
            "custom_rating IS NULL OR (custom_rating >= 1 AND custom_rating <= 5)",
            name=op.f("ck_programs_check_custom_rating"),
        ),
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
        sa.Column("additional_info", sa.String(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.CheckConstraint(
            "(percentage_applicants_interviewed >= 0 AND percentage_applicants_interviewed <= 100)",
            name=op.f(
                "ck_program_statistics_check_percentage_applicants_interviewed"
            ),
        ),
        sa.CheckConstraint(
            "(percentage_non_us_img >= 0 AND percentage_non_us_img <= 100)",
            name=op.f("ck_program_statistics_check_percentage_non_us_img"),
        ),
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
    op.drop_table("directors_peers")
    op.drop_table("directors_alumni")
    op.drop_index(op.f("ix_states_title"), table_name="states")
    op.drop_table("states")
    op.drop_index(op.f("ix_peers_last_name"), table_name="peers")
    op.drop_index(op.f("ix_peers_first_name"), table_name="peers")
    op.drop_table("peers")
    op.drop_index(op.f("ix_directors_last_name"), table_name="directors")
    op.drop_index(op.f("ix_directors_first_name"), table_name="directors")
    op.drop_table("directors")
    op.drop_index(op.f("ix_alumni_last_name"), table_name="alumni")
    op.drop_index(op.f("ix_alumni_first_name"), table_name="alumni")
    op.drop_table("alumni")
    # ### end Alembic commands ###
