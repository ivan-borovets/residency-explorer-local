from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base
from core.models.mixins import AutoTableNameMixin, IntIdPkMixin

if TYPE_CHECKING:
    from .program_statistics import ProgramStatistics


class FurtherTrack(AutoTableNameMixin, IntIdPkMixin, Base):
    # required
    title: Mapped[str] = mapped_column(
        nullable=False,
        unique=True,
        index=True,
    )
    # relationships (many-to-many)
    statistics: Mapped[list["ProgramStatistics"]] = relationship(
        secondary="stats_tracks",
        back_populates="further_tracks",
    )

    def __repr__(self) -> str:
        return f"<FurtherTrack(id={self.id}, title={self.title})>"
