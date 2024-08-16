# mypy: disable-error-code="list-item"
from starlette_admin.contrib.sqla.ext.pydantic import ModelView

from apps.programs.models.directors import Director
from apps.programs.schemas.directors import DirectorIn


class DirectorsView(ModelView):
    exclude_fields_from_create = [
        Director.alumni,
        Director.peers,
    ]


directors_view = DirectorsView(
    model=Director,
    pydantic_model=DirectorIn,
    label="Directors",
)
