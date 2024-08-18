from decimal import Decimal

from pydantic import BaseModel, Field, field_validator

from apps.programs.constants import STR_MIN_LEN
from apps.programs.models.further_tracks import FurtherTrack
from apps.programs.models.programs import Program


class ProgramStatisticsIn(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    # required
    program: Program
    percentage_non_us_img: Decimal = Field(ge=0, le=100)
    # optional
    further_tracks: list[FurtherTrack] | None
    percentage_applicants_interviewed: Decimal | None
    internship_available: bool | None
    more_than_two_russians_interviewed: bool | None
    additional_info: str | None

    # noinspection PyNestedDecorators
    @field_validator("percentage_applicants_interviewed")
    @classmethod
    def check_percentage_applicants_interviewed(
        cls, value: Decimal | None
    ) -> Decimal | None:
        if value is not None and not 0 <= value <= 100:
            raise ValueError(
                "percentage_applicants_interviewed must be between 0 and 100"
            )
        return value

    # noinspection PyNestedDecorators
    @field_validator("additional_info")
    @classmethod
    def check_additional_info(cls, value: str | None) -> str | None:
        if value == "":
            return None
        if value is not None and len(value) < STR_MIN_LEN:
            raise ValueError(
                f"additional_info must be at least {STR_MIN_LEN} characters long"
            )
        return value
