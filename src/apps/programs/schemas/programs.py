from pydantic import BaseModel, Field, field_validator

from apps.programs.constants import STR_MIN_LEN
from apps.programs.models.majors import Major
from apps.programs.models.states import State


class ProgramIn(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    # required
    acgme_id: str = Field(min_length=STR_MIN_LEN)
    title: str = Field(min_length=STR_MIN_LEN)
    city: str = Field(min_length=STR_MIN_LEN)
    major: Major
    state: State
    # optional
    nrmp_code: str | None
    user_rating: int | None
    contact_info: str | None
    additional_info: str | None

    # noinspection PyNestedDecorators
    @field_validator("user_rating")
    @classmethod
    def check_user_rating(cls, value: int | None) -> int | None:
        if value is not None and not 1 <= value <= 5:
            raise ValueError("user_rating must be an integer between 1 and 5")
        return value
