from decimal import Decimal

from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base


class ProgramPgView(Base):
    __tablename__ = "program_view"
    __table_args__ = {"extend_existing": True}

    code: Mapped[str] = mapped_column(
        primary_key=True,
        name="Code",
    )
    title: Mapped[str] = mapped_column(
        nullable=False,
        name="Title",
    )
    city: Mapped[str] = mapped_column(
        nullable=False,
        name="City",
    )
    state: Mapped[str] = mapped_column(
        nullable=False,
        name="State",
    )
    region: Mapped[str] = mapped_column(
        nullable=False,
        name="Region",
    )
    major: Mapped[str] = mapped_column(
        nullable=False,
        name="Major",
    )
    rating: Mapped[int | None] = mapped_column(
        name="Rating",
    )
    percentage_non_us: Mapped[Decimal | None] = mapped_column(
        name="% Non-US",
    )
    percentage_applicants_interviewed: Mapped[Decimal | None] = mapped_column(
        name="% Appl. Int.",
    )
    internship: Mapped[bool | None] = mapped_column(
        name="Internship",
    )
    more_than_two_russians_interviewed: Mapped[bool | None] = mapped_column(
        name=">2 Rus. Int.",
    )
    further_tracks: Mapped[str | None] = mapped_column(
        name="Further Tracks",
    )
    contact_info: Mapped[str | None] = mapped_column(
        name="Contact",
    )
    additional_info: Mapped[str | None] = mapped_column(
        name="Info",
    )
    d_name: Mapped[str | None] = mapped_column(
        name="D. Name",
    )
    d_specialty: Mapped[str | None] = mapped_column(
        name="D. Specialty",
    )
    d_home_country: Mapped[str | None] = mapped_column(
        name="D. Home Country",
    )

    def __repr__(self) -> str:
        return f"<ProgramPGView(code={self.code})>"
