from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from starlette.requests import Request

from core.models import Base
from core.models.mixins import AutoTableNameMixin, IntIdPkMixin

if TYPE_CHECKING:
    from .programs import Program
    from .regions import Region


class State(AutoTableNameMixin, IntIdPkMixin, Base):
    # required
    title: Mapped[str] = mapped_column(
        nullable=False,
        unique=True,
        index=True,
    )
    # foreign keys
    region_id: Mapped[int] = mapped_column(
        ForeignKey("regions.id"),
        nullable=False,
        index=True,
    )
    # relationships (many-to-one)
    region: Mapped["Region"] = relationship(
        back_populates="states",
    )
    # relationships (one-to-many)
    programs: Mapped[list["Program"]] = relationship(
        back_populates="state",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<State(id={self.id}, title={self.title})>"

    async def __admin_repr__(self, request: Request) -> str:
        return f"{self.title}"
