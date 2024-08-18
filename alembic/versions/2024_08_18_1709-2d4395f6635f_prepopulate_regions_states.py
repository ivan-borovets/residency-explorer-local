"""Prepopulate Regions, States

Revision ID: 2d4395f6635f
Revises: b9729e18a48f
Create Date: 2024-08-18 17:09:41.226841

"""

from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.orm import Session

from alembic import op
from apps.programs.data.prepopulate_further_tracks import prepopulate_further_tracks
from apps.programs.data.prepopulate_regions_states import prepopulate_regions_and_states

# revision identifiers, used by Alembic.
revision: str = "2d4395f6635f"
down_revision: Union[str, None] = "b9729e18a48f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    session = Session(bind=bind)

    try:
        prepopulate_regions_and_states(session)
        session.commit()
        prepopulate_further_tracks(session)
        session.commit()
    finally:
        session.close()


def downgrade() -> None:
    pass
