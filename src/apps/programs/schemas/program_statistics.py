from decimal import Decimal
from typing import Annotated

from pydantic import BaseModel, Field, field_validator

from apps.programs.models.program_statistics import FurtherTrack

from .constants.constants import STR_MIN_LEN


class ProgramStatisticsIn(BaseModel):
    percentage_non_us_img: Annotated[Decimal, Field(ge=0, le=100)]
    percentage_applicants_interviewed: Decimal | None
    internship_available: bool | None
    more_than_two_russians_interviewed: bool | None
    predominant_further_track: list[FurtherTrack] | None
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
    @field_validator("predominant_further_track")
    @classmethod
    def check_unique_further_track(
        cls, value: list[FurtherTrack] | None
    ) -> list[FurtherTrack] | None:
        if value and len(value) != len(set(value)):
            raise ValueError("Each FurtherTrack value must be unique")
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
