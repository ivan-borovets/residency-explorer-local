"""Prepopulate States

Revision ID: d713f0ee4e29
Revises: 5ec9fb3a2eb0
Create Date: 2024-08-18 00:37:44.348044

"""

from typing import Sequence, Union

from sqlalchemy.orm import Session

from apps.programs.data.prepopulate_states import prepopulate_states
from apps.programs.data.prepopulate_further_tracks import prepopulate_further_tracks

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d713f0ee4e29"
down_revision: Union[str, None] = "5ec9fb3a2eb0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    session = Session(bind=bind)

    try:
        prepopulate_states(session)
        session.commit()
        prepopulate_further_tracks(session)
        session.commit()
    finally:
        session.close()
    # ### end Alembic commands ###


def downgrade() -> None:
    pass
    # ### end Alembic commands ###
