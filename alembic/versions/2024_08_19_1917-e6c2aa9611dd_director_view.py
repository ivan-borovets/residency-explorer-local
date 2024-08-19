"""director_view

Revision ID: e6c2aa9611dd
Revises: c296c5dd3f8b
Create Date: 2024-08-19 19:17:11.136030

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "e6c2aa9611dd"
down_revision: Union[str, None] = "c296c5dd3f8b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

view_name = "director_view"


def upgrade() -> None:
    view_creation_sql = sa.text(
        f"""
    CREATE VIEW {view_name} AS
        SELECT
            p.code AS "Program Code",
            d.first_name || ' ' || d.last_name AS "Name",       
            d.contact_info AS "Contact",
            d.specialty AS "Specialty",
            d.home_country AS "Home Country",
            d.additional_info AS "Info",
            COUNT(DISTINCT prs.id) AS "N Peers",
            COUNT(DISTINCT a.id) AS "N Alumni"
        FROM
            directors d
        JOIN
            programs p ON p.id = d.program_id
        LEFT JOIN
            directors_peers dp ON dp.director_id = d.id
        LEFT JOIN
            peers prs ON prs.id = dp.peer_id
        LEFT JOIN
            directors_alumni da ON da.director_id = d.id
        LEFT JOIN
            alumni a ON a.id = da.alumni_id
        GROUP BY
            p.code, d.first_name, d.last_name, d.contact_info, d.specialty, d.home_country, d.additional_info;
        """
    )
    op.execute(view_creation_sql)


def downgrade() -> None:
    view_deletion_sql = sa.text(f"DROP VIEW {view_name};")
    op.execute(view_deletion_sql)
