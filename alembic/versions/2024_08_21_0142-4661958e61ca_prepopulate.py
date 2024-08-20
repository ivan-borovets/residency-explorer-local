"""Prepopulate

Revision ID: 4661958e61ca
Revises: 4de87ad54ee2
Create Date: 2024-08-21 01:42:46.795964

"""

from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.orm import Session

from alembic import op
from apps.programs.data.prepopulate_further_tracks import prepopulate_further_tracks
from apps.programs.data.prepopulate_majors import prepopulate_majors
from apps.programs.data.prepopulate_regions_states import prepopulate_regions_and_states

# revision identifiers, used by Alembic.
revision: str = "4661958e61ca"
down_revision: Union[str, None] = "4de87ad54ee2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    session = Session(bind=bind)

    try:
        prepopulate_majors(session)
        session.commit()
        prepopulate_regions_and_states(session)
        session.commit()
        prepopulate_further_tracks(session)
        session.commit()
    finally:
        session.close()


def downgrade() -> None:
    pass
