"""DirectorsPeers+Peers

Revision ID: 68ca4dd3633b
Revises: 400397bb2cc3
Create Date: 2024-08-15 00:32:54.353968

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "68ca4dd3633b"
down_revision: Union[str, None] = "400397bb2cc3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "peers",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.Column("contact_info", sa.String(), nullable=False),
        sa.Column("position", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_peers")),
    )
    op.create_index(op.f("ix_peers_first_name"), "peers", ["first_name"], unique=False)
    op.create_index(op.f("ix_peers_last_name"), "peers", ["last_name"], unique=False)
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
    # ### end Alembic commands ###


def downgrade() -> None:
    op.drop_table("directors_peers")
    op.drop_index(op.f("ix_peers_last_name"), table_name="peers")
    op.drop_index(op.f("ix_peers_first_name"), table_name="peers")
    op.drop_table("peers")
    # ### end Alembic commands ###
