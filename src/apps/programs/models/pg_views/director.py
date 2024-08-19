from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base


class DirectorPgView(Base):
    __tablename__ = "director_view"
    __table_args__ = {"extend_existing": True}

    code: Mapped[str] = mapped_column(
        primary_key=True,
        name="Program Code",
    )
    name: Mapped[str] = mapped_column(
        nullable=False,
        name="Name",
    )
    contact: Mapped[str] = mapped_column(
        nullable=False,
        name="Contact",
    )
    specialty: Mapped[str | None] = mapped_column(
        name="Specialty",
    )
    home_country: Mapped[str | None] = mapped_column(
        name="Home Country",
    )
    info: Mapped[str | None] = mapped_column(
        name="Info",
    )
    n_peers: Mapped[int] = mapped_column(
        name="N Peers",
        nullable=False,
    )
    n_alumni: Mapped[int] = mapped_column(
        name="N Alumni",
        nullable=False,
    )

    def __repr__(self) -> str:
        return f"<DirectorPGView(code={self.code})>"
