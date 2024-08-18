# mypy: disable-error-code="list-item"
from typing import Any, Dict

from starlette.requests import Request
from starlette_admin.contrib.sqla.ext.pydantic import ModelView

from apps.programs.models.regions import Region
from apps.programs.schemas.regions import RegionIn

from .error_handlers.integrity import handle_unique_violation


class RegionsView(ModelView):
    exclude_fields_from_create = [Region.states]
    exclude_fields_from_edit = [Region.states]
    exclude_fields_from_list = [Region.id]

    @handle_unique_violation(schema=RegionIn)
    async def create(self, request: Request, data: Dict[str, Any]) -> Any:
        return await super().create(request, data)

    @handle_unique_violation(schema=RegionIn)
    async def edit(self, request: Request, pk: Any, data: Dict[str, Any]) -> Any:
        return await super().edit(request, pk, data)


regions_view = RegionsView(
    model=Region,
    pydantic_model=RegionIn,
    label="Regions",
)
