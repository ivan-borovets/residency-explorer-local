from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from starlette.requests import Request

from core.models import Base
from core.models.mixins import IntIdPkMixin

if TYPE_CHECKING:
    from .directors import Director


class Alumnus(IntIdPkMixin, Base):
    __tablename__ = "alumni"

    # required
    first_name: Mapped[str] = mapped_column(
        nullable=False,
        index=True,
    )
    last_name: Mapped[str] = mapped_column(
        nullable=False,
        index=True,
    )
    contact_info: Mapped[str] = mapped_column(nullable=False)
    # optional
    work_location: Mapped[str | None] = mapped_column()
    additional_info: Mapped[str | None] = mapped_column()
    # relationships (many-to-many)
    directors: Mapped[list["Director"]] = relationship(
        secondary="directors_alumni",
        back_populates="alumni",
    )

    def __repr__(self) -> str:
        return f"<Alumnus(id={self.id}, name={self.first_name} {self.last_name})>"

    async def __admin_repr__(self, request: Request) -> str:
        return f"{self.first_name} {self.last_name}"
