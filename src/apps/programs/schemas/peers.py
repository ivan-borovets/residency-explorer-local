from pydantic import BaseModel, Field, field_validator

from apps.programs.models.directors import Director

from .constants.constants import STR_MIN_LEN


class PeerIn(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    # required
    directors: list[Director]
    first_name: str = Field(min_length=STR_MIN_LEN)
    last_name: str = Field(min_length=STR_MIN_LEN)
    contact_info: str = Field(min_length=STR_MIN_LEN)
    position: str = Field(min_length=STR_MIN_LEN)

    # noinspection PyNestedDecorators
    @field_validator("directors")
    @classmethod
    def check_directors(cls, value: list[Director]) -> list[Director]:
        if not value:
            raise ValueError("Peer must have at least one director.")
        return value
