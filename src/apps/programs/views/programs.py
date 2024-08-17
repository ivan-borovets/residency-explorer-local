# mypy: disable-error-code="list-item"
from typing import Any, Dict

from starlette.requests import Request
from starlette_admin.contrib.sqla.ext.pydantic import ModelView

from apps.programs.models.programs import Program
from apps.programs.schemas.programs import ProgramIn
from apps.programs.views.error_handlers.integrity import handle_integrity_error


class ProgramsView(ModelView):
    exclude_fields_from_create = [
        Program.director,
        Program.statistics,
    ]

    @handle_integrity_error(schema=ProgramIn)
    async def create(self, request: Request, data: Dict[str, Any]) -> Any:
        return await super().create(request, data)

    @handle_integrity_error(schema=ProgramIn)
    async def edit(self, request: Request, pk: Any, data: Dict[str, Any]) -> Any:
        return await super().edit(request, pk, data)


programs_view = ProgramsView(
    model=Program,
    pydantic_model=ProgramIn,
    label="Programs",
)

# in-place modification
fields_dict = {field.name: field for field in programs_view.fields}
fields_dict["state"].required = True
