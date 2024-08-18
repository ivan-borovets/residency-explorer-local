from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base


class DirectorsAlumnus(Base):
    __tablename__ = "directors_alumni"

    # foreign keys
    director_id: Mapped[int] = mapped_column(
        ForeignKey("directors.id"),
        primary_key=True,
    )
    alumni_id: Mapped[int] = mapped_column(
        ForeignKey("alumni.id"),
        primary_key=True,
    )

    def __repr__(self) -> str:
        return (
            f"<DirectorsAlumnus(director_id={self.director_id}, "
            f"peer_id={self.alumni_id})>"
        )
