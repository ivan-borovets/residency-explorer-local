from pydantic import BaseModel, Field

from apps.programs.constants import STR_MIN_LEN
from apps.programs.models.regions import Region


class StateIn(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    # required
    title: str = Field(min_length=STR_MIN_LEN)
    region: Region
