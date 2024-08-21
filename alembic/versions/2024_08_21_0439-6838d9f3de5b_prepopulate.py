"""Prepopulate

Revision ID: 6838d9f3de5b
Revises: 972abce01dfb
Create Date: 2024-08-21 04:39:52.375706

"""

from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.orm import Session

from alembic import op
from apps.programs.data.prepopulate_further_tracks import prepopulate_further_tracks
from apps.programs.data.prepopulate_majors import prepopulate_majors
from apps.programs.data.prepopulate_regions_states import prepopulate_regions_and_states

# revision identifiers, used by Alembic.
revision: str = "6838d9f3de5b"
down_revision: Union[str, None] = "972abce01dfb"
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
