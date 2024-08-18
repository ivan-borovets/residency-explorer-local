# mypy: disable-error-code="list-item"
from typing import Any, Dict

from starlette.requests import Request
from starlette_admin.contrib.sqla.ext.pydantic import ModelView

from apps.programs.models.program_statistics import ProgramStatistics
from apps.programs.schemas.program_statistics import ProgramStatisticsIn
from apps.programs.views.error_handlers.integrity import handle_not_null_violation


class ProgramStatisticsView(ModelView):
    exclude_fields_from_list = [ProgramStatistics.id]

    @handle_not_null_violation(schema=ProgramStatisticsIn)
    async def create(self, request: Request, data: Dict[str, Any]) -> Any:
        return await super().create(request, data)

    @handle_not_null_violation(schema=ProgramStatisticsIn)
    async def edit(self, request: Request, pk: Any, data: Dict[str, Any]) -> Any:
        return await super().edit(request, pk, data)


program_statistics_view = ProgramStatisticsView(
    model=ProgramStatistics,
    pydantic_model=ProgramStatisticsIn,
    label="Program Statistics",
)

# in-place modification
fields_dict = {field.name: field for field in program_statistics_view.fields}
fields_dict["program"].required = True
fields_dict["percentage_non_us_img"].label = "% Non-US IMG (0.00 - 100.00)"
fields_dict["percentage_applicants_interviewed"].label = (
    "% Applicants Interviewed (0.00 - 100.00)"
)
