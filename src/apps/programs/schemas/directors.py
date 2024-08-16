from pydantic import BaseModel, Field, field_validator

from apps.programs.models.programs import Program

from .constants.constants import STR_MIN_LEN


class DirectorIn(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    # required
    first_name: str = Field(min_length=STR_MIN_LEN)
    last_name: str = Field(min_length=STR_MIN_LEN)
    contact_info: str = Field(min_length=STR_MIN_LEN)
    program: Program
    # optional
    specialty: str | None
    home_country: str | None
    additional_info: str | None

    # noinspection PyNestedDecorators
    @field_validator("specialty")
    @classmethod
    def check_specialty(cls, value: str | None) -> str | None:
        if value == "":
            return None
        if value is not None and len(value) < STR_MIN_LEN:
            raise ValueError(
                f"specialty must be at least {STR_MIN_LEN} characters long"
            )
        return value

    # noinspection PyNestedDecorators
    @field_validator("home_country")
    @classmethod
    def check_home_country(cls, value: str | None) -> str | None:
        if value == "":
            return None
        if value is not None and len(value) < STR_MIN_LEN:
            raise ValueError(
                f"home_country must be at least {STR_MIN_LEN} characters long"
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
