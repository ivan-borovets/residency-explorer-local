# mypy: disable-error-code="list-item"
from typing import Any, Dict

from starlette.requests import Request
from starlette_admin.contrib.sqla.ext.pydantic import ModelView

from apps.programs.models.states import State
from apps.programs.schemas.states import StateIn

from .error_handlers.integrity import handle_integrity_error


class StatesView(ModelView):
    exclude_fields_from_create = [State.programs]

    @handle_integrity_error(schema=StateIn)
    async def create(self, request: Request, data: Dict[str, Any]) -> Any:
        return await super().create(request, data)

    @handle_integrity_error(schema=StateIn)
    async def edit(self, request: Request, pk: Any, data: Dict[str, Any]) -> Any:
        return await super().edit(request, pk, data)


states_view = StatesView(
    model=State,
    pydantic_model=StateIn,
    label="States & Regions",
)
