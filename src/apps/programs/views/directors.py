# mypy: disable-error-code="list-item"
from typing import Any, Dict

from starlette.requests import Request
from starlette_admin.contrib.sqla.ext.pydantic import ModelView

from apps.programs.models.directors import Director
from apps.programs.schemas.directors import DirectorIn
from apps.programs.views.error_handlers.integrity import handle_not_null_violation


class DirectorsView(ModelView):
    exclude_fields_from_create = [
        Director.alumni,
        Director.peers,
    ]
    exclude_fields_from_edit = [
        Director.alumni,
        Director.peers,
    ]
    exclude_fields_from_list = [Director.id]

    @handle_not_null_violation(schema=DirectorIn)
    async def create(self, request: Request, data: Dict[str, Any]) -> Any:
        return await super().create(request, data)

    @handle_not_null_violation(schema=DirectorIn)
    async def edit(self, request: Request, pk: Any, data: Dict[str, Any]) -> Any:
        return await super().edit(request, pk, data)


directors_view = DirectorsView(
    model=Director,
    pydantic_model=DirectorIn,
    label="Directors",
)

# in-place modification
fields_dict = {field.name: field for field in directors_view.fields}
fields_dict["program"].required = True
