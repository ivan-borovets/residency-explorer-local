from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base
from core.models.mixins import IntIdPkMixin

if TYPE_CHECKING:
    from .further_tracks import FurtherTrack
    from .programs import Program


CHECK_PERCENTAGE_NON_US_IMG = (
    "(percentage_non_us_img >= 0 AND percentage_non_us_img <= 100)"
)
CHECK_PERCENTAGE_APPLICANTS_INTERVIEWED = (
    "(percentage_applicants_interviewed >= 0 AND "
    "percentage_applicants_interviewed <= 100)"
)


class ProgramStatistics(IntIdPkMixin, Base):
    __tablename__ = "program_statistics"

    # required
    percentage_non_us_img: Mapped[Decimal] = mapped_column(nullable=False)
    # foreign keys
    program_id: Mapped[int] = mapped_column(
        ForeignKey("programs.id"),
    )
    # optional
    percentage_applicants_interviewed: Mapped[Decimal | None] = mapped_column()
    internship_available: Mapped[bool | None] = mapped_column()
    more_than_two_russians_interviewed: Mapped[bool | None] = mapped_column()
    additional_info: Mapped[str | None] = mapped_column()
    # constraints
    __table_args__ = (
        CheckConstraint(
            sqltext=CHECK_PERCENTAGE_NON_US_IMG,
            name="check_percentage_non_us_img",
        ),
        CheckConstraint(
            sqltext=CHECK_PERCENTAGE_APPLICANTS_INTERVIEWED,
            name="check_percentage_applicants_interviewed",
        ),
    )
    # relationships (one-to-one)
    program: Mapped["Program"] = relationship(
        back_populates="statistics", uselist=False
    )
    # relationships (many-to-many)
    further_tracks: Mapped[list["FurtherTrack"]] = relationship(
        secondary="stats_tracks",
        back_populates="statistics",
    )

    def __repr__(self) -> str:
        return f"<ProgramStatistics(id={self.id})>"
