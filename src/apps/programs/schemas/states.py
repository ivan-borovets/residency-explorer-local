from pydantic import BaseModel, Field

from .constants.constants import STR_MIN_LEN


class StateIn(BaseModel):
    title: str = Field(min_length=STR_MIN_LEN)
    region: str = Field(min_length=STR_MIN_LEN)
