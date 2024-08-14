from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from core.models.mixins import AutoTableNameMixin, IntIdPkMixin


class Program(AutoTableNameMixin, IntIdPkMixin, Base):
    code: Mapped[str] = mapped_column(nullable=False, unique=True, index=True)
    title: Mapped[str] = mapped_column(nullable=False)
    city: Mapped[str] = mapped_column(nullable=False)
    # foreign keys
    state_id: Mapped[int] = mapped_column(
        ForeignKey("states.id"), nullable=False, index=True
    )
    director_id: Mapped[int] = mapped_column(
        ForeignKey("directors.id"), nullable=False, index=True
    )

    def __repr__(self) -> str:
        return f"<Program(id={self.id}, code={self.code}, title='{self.title}')>"
