from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base
from core.models.mixins import AutoTableNameMixin, IntIdPkMixin

if TYPE_CHECKING:
    from .directors import Director


class Peer(AutoTableNameMixin, IntIdPkMixin, Base):
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
    position: Mapped[str] = mapped_column(nullable=False)
    # relationships (many-to-many)
    directors: Mapped[list["Director"]] = relationship(
        secondary="directors_peers",
        back_populates="peers",
    )

    def __repr__(self) -> str:
        return f"<Peer(id={self.id}, name={self.first_name} {self.last_name}')>"
