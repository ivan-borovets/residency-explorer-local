# mypy: disable-error-code="list-item"
from starlette_admin.contrib.sqla.ext.pydantic import ModelView

from apps.programs.models.peers import Peer
from apps.programs.schemas.peers import PeerIn


class PeersView(ModelView):
    exclude_fields_from_list = [Peer.id]


peers_view = PeersView(
    model=Peer,
    pydantic_model=PeerIn,
    label="Directors' Peers",
)

# in-place modification
fields_dict = {field.name: field for field in peers_view.fields}
fields_dict["directors"].required = True
