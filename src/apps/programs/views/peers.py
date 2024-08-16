from starlette_admin.contrib.sqla.ext.pydantic import ModelView

from apps.programs.models.peers import Peer
from apps.programs.schemas.peers import PeerIn

peers_view = ModelView(
    model=Peer,
    pydantic_model=PeerIn,
    label="Directors' Peers",
)
