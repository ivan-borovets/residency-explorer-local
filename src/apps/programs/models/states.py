from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base
from core.models.mixins import AutoTableNameMixin, IntIdPkMixin

if TYPE_CHECKING:
    from .programs import Program


class State(AutoTableNameMixin, IntIdPkMixin, Base):
    title: Mapped[str] = mapped_column(nullable=False, index=True)
    region: Mapped[str] = mapped_column(nullable=False)
    # relationships
    programs: Mapped[list["Program"]] = relationship(
        back_populates="state", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<State(id={self.id}, title={self.title}, region='{self.region}')>"
