from pydantic import BaseModel, Field

from .constants.constants import STR_MIN_LEN


class RegionIn(BaseModel):
    # required
    title: str = Field(min_length=STR_MIN_LEN)
