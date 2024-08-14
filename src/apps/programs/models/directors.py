from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from core.models.mixins import AutoTableNameMixin, IntIdPkMixin


class Director(AutoTableNameMixin, IntIdPkMixin, Base):
    first_name: Mapped[str] = mapped_column(nullable=False, index=True)
    last_name: Mapped[str] = mapped_column(nullable=False, index=True)
    contact_info: Mapped[str] = mapped_column(nullable=False)
    specialty: Mapped[str | None] = mapped_column()
    home_country: Mapped[str | None] = mapped_column()
    additional_info: Mapped[str | None] = mapped_column()

    def __repr__(self) -> str:
        return f"<Director(id={self.id}, name={self.first_name} {self.last_name}')>"
