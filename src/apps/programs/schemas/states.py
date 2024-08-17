from pydantic import BaseModel, Field

from apps.programs.models.regions import Region

from .constants.constants import STR_MIN_LEN


class StateIn(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    # required
    title: str = Field(min_length=STR_MIN_LEN)
    region: Region
