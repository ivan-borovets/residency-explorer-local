from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base
from core.models.mixins import AutoTableNameMixin, IntIdPkMixin

if TYPE_CHECKING:
    from .states import State


class Region(AutoTableNameMixin, IntIdPkMixin, Base):
    # required
    title: Mapped[str] = mapped_column(
        nullable=False,
        unique=True,
        index=True,
    )
    # relationships (one-to-many)
    states: Mapped[list["State"]] = relationship(
        back_populates="region",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<Region(id={self.id}, title={self.title}')>"
