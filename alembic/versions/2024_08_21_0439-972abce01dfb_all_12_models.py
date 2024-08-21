"""All 12 models

Revision ID: 972abce01dfb
Revises: 
Create Date: 2024-08-21 04:39:13.734683

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "972abce01dfb"
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
        sa.Column("additional_info", sa.String(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_alumni")),
    )
    op.create_index(
        op.f("ix_alumni_first_name"), "alumni", ["first_name"], unique=False
    )
    op.create_index(op.f("ix_alumni_last_name"), "alumni", ["last_name"], unique=False)
    op.create_table(
        "further_tracks",
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_further_tracks")),
    )
    op.create_index(
        op.f("ix_further_tracks_title"),
        "further_tracks",
        ["title"],
        unique=True,
    )
    op.create_table(
        "majors",
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_majors")),
    )
    op.create_index(op.f("ix_majors_title"), "majors", ["title"], unique=False)
    op.create_table(
        "peers",
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.Column("contact_info", sa.String(), nullable=False),
        sa.Column("position", sa.String(), nullable=False),
        sa.Column("additional_info", sa.String(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_peers")),
    )
    op.create_index(op.f("ix_peers_first_name"), "peers", ["first_name"], unique=False)
    op.create_index(op.f("ix_peers_last_name"), "peers", ["last_name"], unique=False)
    op.create_table(
        "regions",
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_regions")),
    )
    op.create_index(op.f("ix_regions_title"), "regions", ["title"], unique=True)
    op.create_table(
        "states",
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("region_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["region_id"],
            ["regions.id"],
            name=op.f("fk_states_region_id_regions"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_states")),
    )
    op.create_index(op.f("ix_states_region_id"), "states", ["region_id"], unique=False)
    op.create_index(op.f("ix_states_title"), "states", ["title"], unique=True)
    op.create_table(
        "programs",
        sa.Column("acgme_id", sa.String(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("city", sa.String(), nullable=False),
        sa.Column("major_id", sa.Integer(), nullable=False),
        sa.Column("state_id", sa.Integer(), nullable=False),
        sa.Column("nrmp_code", sa.String(), nullable=True),
        sa.Column("user_rating", sa.Integer(), nullable=True),
        sa.Column("contact_info", sa.String(), nullable=True),
        sa.Column("additional_info", sa.String(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.CheckConstraint(
            "user_rating IS NULL OR (user_rating >= 1 AND user_rating <= 5)",
            name=op.f("ck_programs_check_user_rating"),
        ),
        sa.ForeignKeyConstraint(
            ["major_id"],
            ["majors.id"],
            name=op.f("fk_programs_major_id_majors"),
        ),
        sa.ForeignKeyConstraint(
            ["state_id"],
            ["states.id"],
            name=op.f("fk_programs_state_id_states"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_programs")),
    )
    op.create_index(op.f("ix_programs_acgme_id"), "programs", ["acgme_id"], unique=True)
    op.create_index(
        op.f("ix_programs_major_id"), "programs", ["major_id"], unique=False
    )
    op.create_index(
        op.f("ix_programs_state_id"), "programs", ["state_id"], unique=False
    )
    op.create_table(
        "directors",
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.Column("contact_info", sa.String(), nullable=False),
        sa.Column("program_id", sa.Integer(), nullable=False),
        sa.Column("specialty", sa.String(), nullable=True),
        sa.Column("home_country", sa.String(), nullable=True),
        sa.Column("additional_info", sa.String(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["program_id"],
            ["programs.id"],
            name=op.f("fk_directors_program_id_programs"),
        ),
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
    op.create_index(
        op.f("ix_directors_program_id"),
        "directors",
        ["program_id"],
        unique=False,
    )
    op.create_table(
        "program_statistics",
        sa.Column("percentage_non_us_img", sa.Numeric(), nullable=False),
        sa.Column("program_id", sa.Integer(), nullable=False),
        sa.Column("percentage_applicants_interviewed", sa.Numeric(), nullable=True),
        sa.Column("internship_available", sa.Boolean(), nullable=True),
        sa.Column("more_than_two_russians_interviewed", sa.Boolean(), nullable=True),
        sa.Column("additional_info", sa.String(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.CheckConstraint(
            "(percentage_applicants_interviewed >= 0 AND percentage_applicants_interviewed <= 100)",
            name=op.f("ck_program_statistics_check_percentage_applicants_interviewed"),
        ),
        sa.CheckConstraint(
            "(percentage_non_us_img >= 0 AND percentage_non_us_img <= 100)",
            name=op.f("ck_program_statistics_check_percentage_non_us_img"),
        ),
        sa.ForeignKeyConstraint(
            ["program_id"],
            ["programs.id"],
            name=op.f("fk_program_statistics_program_id_programs"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_program_statistics")),
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
        "stats_tracks",
        sa.Column("stat_id", sa.Integer(), nullable=False),
        sa.Column("track_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["stat_id"],
            ["program_statistics.id"],
            name=op.f("fk_stats_tracks_stat_id_program_statistics"),
        ),
        sa.ForeignKeyConstraint(
            ["track_id"],
            ["further_tracks.id"],
            name=op.f("fk_stats_tracks_track_id_further_tracks"),
        ),
        sa.PrimaryKeyConstraint("stat_id", "track_id", name=op.f("pk_stats_tracks")),
    )


def downgrade() -> None:
    op.drop_table("stats_tracks")
    op.drop_table("directors_peers")
    op.drop_table("directors_alumni")
    op.drop_table("program_statistics")
    op.drop_index(op.f("ix_directors_program_id"), table_name="directors")
    op.drop_index(op.f("ix_directors_last_name"), table_name="directors")
    op.drop_index(op.f("ix_directors_first_name"), table_name="directors")
    op.drop_table("directors")
    op.drop_index(op.f("ix_programs_state_id"), table_name="programs")
    op.drop_index(op.f("ix_programs_major_id"), table_name="programs")
    op.drop_index(op.f("ix_programs_acgme_id"), table_name="programs")
    op.drop_table("programs")
    op.drop_index(op.f("ix_states_title"), table_name="states")
    op.drop_index(op.f("ix_states_region_id"), table_name="states")
    op.drop_table("states")
    op.drop_index(op.f("ix_regions_title"), table_name="regions")
    op.drop_table("regions")
    op.drop_index(op.f("ix_peers_last_name"), table_name="peers")
    op.drop_index(op.f("ix_peers_first_name"), table_name="peers")
    op.drop_table("peers")
    op.drop_index(op.f("ix_majors_title"), table_name="majors")
    op.drop_table("majors")
    op.drop_index(op.f("ix_further_tracks_title"), table_name="further_tracks")
    op.drop_table("further_tracks")
    op.drop_index(op.f("ix_alumni_last_name"), table_name="alumni")
    op.drop_index(op.f("ix_alumni_first_name"), table_name="alumni")
    op.drop_table("alumni")
