from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base
from core.models.mixins import AutoTableNameMixin, IntIdPkMixin

if TYPE_CHECKING:
    from .alumni import Alumnus
    from .peers import Peer
    from .programs import Program


class Director(AutoTableNameMixin, IntIdPkMixin, Base):
    first_name: Mapped[str] = mapped_column(nullable=False, index=True)
    last_name: Mapped[str] = mapped_column(nullable=False, index=True)
    contact_info: Mapped[str] = mapped_column(nullable=False)
    specialty: Mapped[str | None] = mapped_column()
    home_country: Mapped[str | None] = mapped_column()
    additional_info: Mapped[str | None] = mapped_column()
    # relationships
    alumni: Mapped[list["Alumnus"]] = relationship(
        secondary="directors_alumni", back_populates="directors"
    )
    peers: Mapped[list["Peer"]] = relationship(
        secondary="directors_peers", back_populates="directors"
    )
    program: Mapped["Program"] = relationship(back_populates="director", uselist=False)

    def __repr__(self) -> str:
        return f"<Director(id={self.id}, name={self.first_name} {self.last_name}')>"
