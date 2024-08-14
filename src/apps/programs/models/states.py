from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from core.models.mixins import AutoTableNameMixin, IntIdPkMixin


class State(AutoTableNameMixin, IntIdPkMixin, Base):
    title: Mapped[str] = mapped_column(nullable=False, index=True)
    region: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return f"<State(id={self.id}, title={self.title}, region='{self.region}')>"
