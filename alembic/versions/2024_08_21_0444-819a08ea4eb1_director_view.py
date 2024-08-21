"""Director View

Revision ID: 819a08ea4eb1
Revises: 6838d9f3de5b
Create Date: 2024-08-21 04:44:13.074584

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "819a08ea4eb1"
down_revision: Union[str, None] = "6838d9f3de5b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

view_name = "director_view"


def upgrade() -> None:
    view_creation_sql = sa.text(
        f"""
        CREATE VIEW {view_name} AS
            SELECT
                p.acgme_id AS "ACGME ID",
                p.nrmp_code AS "NRMP Code",
                d.first_name || ' ' || d.last_name AS "Name",       
                d.contact_info AS "Contact",
                d.specialty AS "Specialty",
                d.home_country AS "Home Country",
                COUNT(DISTINCT prs.id) AS "N Peers",
                COUNT(DISTINCT a.id) AS "N Alumni",
                d.additional_info AS "Info"
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
                p.acgme_id, p.nrmp_code, 
                d.first_name, d.last_name, 
                d.contact_info, d.specialty, 
                d.home_country, d.additional_info;
        """
    )
    op.execute(view_creation_sql)


def downgrade() -> None:
    view_deletion_sql = sa.text(f"DROP VIEW {view_name};")
    op.execute(view_deletion_sql)
