from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from core.models.mixins import IntIdPkMixin


class Alumnus(IntIdPkMixin, Base):
    __tablename__ = "alumni"

    first_name: Mapped[str] = mapped_column(nullable=False, index=True)
    last_name: Mapped[str] = mapped_column(nullable=False, index=True)
    contact_info: Mapped[str] = mapped_column(nullable=False)
    work_location: Mapped[str | None] = mapped_column()

    def __repr__(self) -> str:
        return f"<Alumnus(id={self.id}, name={self.first_name} {self.last_name}')>"
