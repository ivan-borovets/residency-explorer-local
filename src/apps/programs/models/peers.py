from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from core.models.mixins import AutoTableNameMixin, IntIdPkMixin


class Peer(AutoTableNameMixin, IntIdPkMixin, Base):
    first_name: Mapped[str] = mapped_column(nullable=False, index=True)
    last_name: Mapped[str] = mapped_column(nullable=False, index=True)
    contact_info: Mapped[str] = mapped_column(nullable=False)
    position: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return f"<Peer(id={self.id}, name={self.first_name} {self.last_name}')>"
