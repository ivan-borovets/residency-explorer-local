from pydantic import BaseModel, Field

from apps.programs.constants import STR_MIN_LEN


class RegionIn(BaseModel):
    # required
    title: str = Field(min_length=STR_MIN_LEN)
