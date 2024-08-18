from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from core.models.mixins import AutoTableNameMixin


class DirectorsPeer(AutoTableNameMixin, Base):
    # foreign keys
    director_id: Mapped[int] = mapped_column(
        ForeignKey("directors.id"),
        primary_key=True,
    )
    peer_id: Mapped[int] = mapped_column(
        ForeignKey("peers.id"),
        primary_key=True,
    )

    def __repr__(self) -> str:
        return (
            f"<DirectorsPeer(director_id={self.director_id}, peer_id={self.peer_id})>"
        )
