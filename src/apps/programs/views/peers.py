from starlette_admin import ExportType, HasMany, IntegerField, StringField
from starlette_admin.contrib.sqla.ext.pydantic import ModelView

from apps.programs.constants import STR_MIN_LEN
from apps.programs.models.peers import Peer
from apps.programs.schemas.peers import PeerIn


class PeersView(ModelView):
    fields = [
        IntegerField(
            # BaseField
            name="id",
            label="Id",
            exclude_from_list=True,
            exclude_from_detail=True,
        ),
        StringField(
            # BaseField
            name="first_name",
            label="First name",
            required=True,
            # StringField
            minlength=STR_MIN_LEN,
            placeholder="John",
        ),
        StringField(
            # BaseField
            name="last_name",
            label="Last name",
            required=True,
            # StringField
            minlength=STR_MIN_LEN,
            placeholder="Doe",
        ),
        StringField(
            # BaseField
            name="contact_info",
            label="Contact info",
            required=True,
            # StringField
            minlength=STR_MIN_LEN,
            placeholder="+1 (555) 123-4567, "
            "john.doe@example.com, "
            "123 Main St, Springfield, IL",
        ),
        StringField(
            # BaseField
            name="position",
            label="Position",
            required=True,
            # StringField
            minlength=STR_MIN_LEN,
            placeholder="Program coordinator",
        ),
        HasMany(
            # BaseField
            name="directors",
            label="Directors",
            required=True,
            # RelationField
            identity="director",
        ),
    ]

    # initial order
    fields_default_sort = ["first_name"]  # ascending

    export_types = [
        ExportType.CSV,
        ExportType.EXCEL,
        ExportType.PDF,
        ExportType.PRINT,
    ]


peers_view = PeersView(
    model=Peer,
    pydantic_model=PeerIn,
    label="Directors' Peers",
)
