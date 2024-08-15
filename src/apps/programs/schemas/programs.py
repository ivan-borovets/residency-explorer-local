from pydantic import BaseModel, Field, field_validator

from .constants.constants import STR_MIN_LEN


class ProgramIn(BaseModel):
    code: str = Field(min_length=STR_MIN_LEN)
    title: str = Field(min_length=STR_MIN_LEN)
    city: str = Field(min_length=STR_MIN_LEN)
    custom_rating: int | None

    # noinspection PyNestedDecorators
    @field_validator("custom_rating")
    @classmethod
    def check_custom_rating(cls, value: int | None) -> int | None:
        if value is not None and not 1 <= value <= 5:
            raise ValueError("custom_rating must be an integer between 1 and 5")
        return value
