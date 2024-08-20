"""Program View

Revision ID: 1b8686bd6757
Revises: 9c8ab297443a
Create Date: 2024-08-21 01:47:32.614147

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "1b8686bd6757"
down_revision: Union[str, None] = "9c8ab297443a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

view_name = "program_view"


def upgrade() -> None:
    view_creation_sql = sa.text(
        f"""
        CREATE VIEW {view_name} AS
            SELECT
                p.code AS "Code",
                p.title AS "Title",
                p.city AS "City",
                s.title AS "State",
                r.title AS "Region",
                m.title AS "Major",
                p.user_rating AS "Rating",
                ps.percentage_non_us_img AS "% Non-US",
                ps.percentage_applicants_interviewed AS "% Appl. Int.",
                ps.internship_available AS "Internship",
                ps.more_than_two_russians_interviewed AS ">2 Rus. Int.",
                STRING_AGG(ft.title, ', ') AS "Further Tracks",
                p.contact_info AS "Contact",
                p.additional_info AS "Info",
                d.first_name || ' ' || d.last_name AS "D. Name",
                d.specialty AS "D. Specialty",
                d.home_country AS "D. Home Country"
            FROM
                programs p
            LEFT JOIN
                majors m ON m.id = p.major_id
            LEFT JOIN
                states s ON s.id = p.state_id
            LEFT JOIN
                regions r ON r.id = s.region_id
            LEFT JOIN
                program_statistics ps ON ps.program_id = p.id
            LEFT JOIN
                stats_tracks st ON st.stat_id = ps.id
            LEFT JOIN
                further_tracks ft ON ft.id = st.track_id
            LEFT JOIN
                directors d ON d.program_id = p.id
            GROUP BY
                p.code, p.title, p.city, m.title, s.title, r.title, 
                p.user_rating, ps.percentage_non_us_img, ps.percentage_applicants_interviewed,
                ps.internship_available, ps.more_than_two_russians_interviewed,
                p.contact_info, p.additional_info,
                d.first_name, d.last_name, d.specialty, d.home_country;
        """
    )
    op.execute(view_creation_sql)


def downgrade() -> None:
    view_deletion_sql = sa.text(f"DROP VIEW {view_name};")
    op.execute(view_deletion_sql)
