from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from starlette.requests import Request

from core.models import Base
from core.models.mixins import AutoTableNameMixin, IntIdPkMixin

if TYPE_CHECKING:
    from .alumni import Alumnus
    from .peers import Peer
    from .programs import Program


class Director(AutoTableNameMixin, IntIdPkMixin, Base):
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
    # foreign keys
    program_id: Mapped[int] = mapped_column(
        ForeignKey("programs.id"),
        nullable=False,
        index=True,
    )
    # optional
    specialty: Mapped[str | None] = mapped_column()
    home_country: Mapped[str | None] = mapped_column()
    additional_info: Mapped[str | None] = mapped_column()
    # relationships (one-to-one)
    program: Mapped["Program"] = relationship(
        back_populates="director",
        uselist=False,
    )
    # relationships (many-to-many)
    alumni: Mapped[list["Alumnus"]] = relationship(
        secondary="directors_alumni",
        back_populates="directors",
    )
    peers: Mapped[list["Peer"]] = relationship(
        secondary="directors_peers",
        back_populates="directors",
    )

    def __repr__(self) -> str:
        return f"<Director(id={self.id}, name={self.first_name} {self.last_name})>"

    async def __admin_repr__(self, request: Request) -> str:
        return f"{self.first_name} {self.last_name}"
