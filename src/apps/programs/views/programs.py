# mypy: disable-error-code="list-item"
from starlette_admin.contrib.sqla.ext.pydantic import ModelView

from apps.programs.models.programs import Program
from apps.programs.schemas.programs import ProgramIn


class ProgramsView(ModelView):
    exclude_fields_from_create = [
        Program.director,
        Program.statistics,
    ]


programs_view = ProgramsView(
    model=Program,
    pydantic_model=ProgramIn,
    label="Programs",
)
