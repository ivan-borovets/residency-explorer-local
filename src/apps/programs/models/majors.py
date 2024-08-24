from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from starlette.requests import Request

from core.models import Base
from core.models.mixins import AutoTableNameMixin, IntIdPkMixin

if TYPE_CHECKING:
    from .programs import Program


class Major(AutoTableNameMixin, IntIdPkMixin, Base):
    # required
    title: Mapped[str] = mapped_column(
        nullable=False,
        index=True,
    )
    # relationships (one-to-many)
    programs: Mapped[list["Program"]] = relationship(
        back_populates="major",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<Major(id={self.id}, title={self.title})>"

    async def __admin_repr__(self, request: Request) -> str:
        return f"{self.title}"
