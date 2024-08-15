from pydantic import BaseModel, Field, field_validator

from .constants.constants import STR_MIN_LEN


class AlumniIn(BaseModel):
    first_name: str = Field(min_length=STR_MIN_LEN)
    last_name: str = Field(min_length=STR_MIN_LEN)
    contact_info: str = Field(min_length=STR_MIN_LEN)
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
