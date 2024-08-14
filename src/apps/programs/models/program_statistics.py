from decimal import Decimal
from enum import Enum as Python_Enum
from typing import TYPE_CHECKING

from sqlalchemy import ARRAY, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base

if TYPE_CHECKING:
    from .programs import Program


class FurtherTrack(Python_Enum):
    ACADEMIC = "academic"
    FULLTIME = "full-time"
    RESIDENCY = "residency"
    OTHER = "other"


def list_enum_values(enum_input: Python_Enum) -> list:
    return [e.value for e in enum_input]  # type: ignore


class ProgramStatistics(Base):
    __tablename__ = "program_statistics"

    percentage_non_us_img: Mapped[Decimal] = mapped_column(nullable=False)
    percentage_applicants_interviewed: Mapped[Decimal | None] = mapped_column()
    internship_available: Mapped[bool | None] = mapped_column()
    more_than_two_russians_interviewed: Mapped[bool | None] = mapped_column()
    predominant_further_track: Mapped[list[str] | None] = mapped_column(
        ARRAY(
            Enum(
                FurtherTrack,
                name="further_track_enum",
                values_callable=list_enum_values,
            )
        )
    )
    additional_info: Mapped[str] = mapped_column()
    # foreign keys
    id: Mapped[int] = mapped_column(ForeignKey("programs.id"), primary_key=True)
    # relationships
    program: Mapped["Program"] = relationship(
        back_populates="statistics", uselist=False
    )

    def __repr__(self) -> str:
        return f"<ProgramStatistics(id={self.id}')>"
