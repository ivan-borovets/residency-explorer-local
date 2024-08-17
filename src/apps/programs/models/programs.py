from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base
from core.models.mixins import AutoTableNameMixin, IntIdPkMixin

if TYPE_CHECKING:
    from .directors import Director
    from .program_statistics import ProgramStatistics
    from .states import State

CHECK_CUSTOM_RATING = (
    "custom_rating IS NULL OR (custom_rating >= 1 AND custom_rating <= 5)"
)


class Program(AutoTableNameMixin, IntIdPkMixin, Base):
    # required
    code: Mapped[str] = mapped_column(
        nullable=False,
        unique=True,
        index=True,
    )
    title: Mapped[str] = mapped_column(nullable=False)
    city: Mapped[str] = mapped_column(nullable=False)
    # foreign keys
    state_id: Mapped[int] = mapped_column(
        ForeignKey("states.id"),
        nullable=False,
        index=True,
    )
    # optional
    user_rating: Mapped[int | None] = mapped_column()
    # constraints
    __table_args__ = (
        CheckConstraint(
            sqltext=CHECK_CUSTOM_RATING,
            name="check_custom_rating",
        ),
    )
    # relationships (one-to-one)
    director: Mapped["Director"] = relationship(
        back_populates="program",
        uselist=False,
    )
    statistics: Mapped["ProgramStatistics"] = relationship(
        back_populates="program",
        uselist=False,
    )
    # relationships (many-to-one)
    state: Mapped["State"] = relationship(back_populates="programs")

    def __repr__(self) -> str:
        return f"<Program(id={self.id}, code={self.code}, title='{self.title}')>"
