"""Fix State, FurtherTrack models

Revision ID: 6bf2810bcca8
Revises: 3d5318fd5a53
Create Date: 2024-08-17 22:26:51.446680

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6bf2810bcca8"
down_revision: Union[str, None] = "3d5318fd5a53"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_index("ix_further_tracks_title", table_name="further_tracks")
    op.create_index(
        op.f("ix_further_tracks_title"),
        "further_tracks",
        ["title"],
        unique=True,
    )
    op.drop_index("ix_states_title", table_name="states")
    op.create_index(op.f("ix_states_title"), "states", ["title"], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    op.drop_index(op.f("ix_states_title"), table_name="states")
    op.create_index("ix_states_title", "states", ["title"], unique=False)
    op.drop_index(op.f("ix_further_tracks_title"), table_name="further_tracks")
    op.create_index(
        "ix_further_tracks_title", "further_tracks", ["title"], unique=False
    )
    # ### end Alembic commands ###
