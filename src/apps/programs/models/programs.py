from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base
from core.models.mixins import AutoTableNameMixin, IntIdPkMixin

if TYPE_CHECKING:
    from .directors import Director
    from .program_statistics import ProgramStatistics
    from .states import State


class Program(AutoTableNameMixin, IntIdPkMixin, Base):
    code: Mapped[str] = mapped_column(nullable=False, unique=True, index=True)
    title: Mapped[str] = mapped_column(nullable=False)
    city: Mapped[str] = mapped_column(nullable=False)
    custom_rating: Mapped[int | None] = mapped_column()
    # constraints
    __table_args__ = (
        CheckConstraint(
            "custom_rating IS NULL OR (custom_rating >= 1 AND custom_rating <= 10)",
            name="check_custom_rating",
        ),
    )

    # foreign keys
    state_id: Mapped[int] = mapped_column(
        ForeignKey("states.id"), nullable=False, index=True
    )
    director_id: Mapped[int] = mapped_column(
        ForeignKey("directors.id"), nullable=False, index=True
    )
    # relationships
    director: Mapped["Director"] = relationship(back_populates="program", uselist=False)
    state: Mapped["State"] = relationship(back_populates="programs")
    statistics: Mapped["ProgramStatistics"] = relationship(
        back_populates="program", uselist=False
    )

    def __repr__(self) -> str:
        return f"<Program(id={self.id}, code={self.code}, title='{self.title}')>"
