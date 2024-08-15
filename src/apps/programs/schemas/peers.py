from pydantic import BaseModel, Field

from .constants.constants import STR_MIN_LEN


class PeerIn(BaseModel):
    first_name: str = Field(min_length=STR_MIN_LEN)
    last_name: str = Field(min_length=STR_MIN_LEN)
    contact_info: str = Field(min_length=STR_MIN_LEN)
    position: str = Field(min_length=STR_MIN_LEN)
