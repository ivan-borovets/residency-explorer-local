from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base


class StatsTrack(Base):
    __tablename__ = "stats_tracks"

    # foreign keys
    stat_id: Mapped[int] = mapped_column(
        ForeignKey("program_statistics.id"),
        primary_key=True,
    )
    track_id: Mapped[int] = mapped_column(
        ForeignKey("further_tracks.id"),
        primary_key=True,
    )

    def __repr__(self) -> str:
        return f"<StatsTrack(stat_id={self.stat_id}, track_id={self.track_id}')>"
