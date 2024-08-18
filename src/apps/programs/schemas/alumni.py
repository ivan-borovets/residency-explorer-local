from pydantic import BaseModel, Field, field_validator

from apps.programs.constants import STR_MIN_LEN
from apps.programs.models.directors import Director


class AlumniIn(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    # required
    directors: list[Director]
    first_name: str = Field(min_length=STR_MIN_LEN)
    last_name: str = Field(min_length=STR_MIN_LEN)
    contact_info: str = Field(min_length=STR_MIN_LEN)
    # optional
    work_location: str | None

    # noinspection PyNestedDecorators
    @field_validator("work_location")
    @classmethod
    def check_work_location(cls, value: str | None) -> str | None:
        if value == "":
            return None
        if value is not None and len(value) < STR_MIN_LEN:
            raise ValueError(
                f"work_location must be at least {STR_MIN_LEN} characters long"
            )
        return value

    # noinspection PyNestedDecorators
    @field_validator("directors")
    @classmethod
    def check_directors(cls, value: list[Director]) -> list[Director]:
        if not value:
            raise ValueError("Alumnus must have at least one director.")
        return value
