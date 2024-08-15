from starlette_admin.contrib.sqla.ext.pydantic import ModelView

from apps.programs.models.programs import Program
from apps.programs.schemas.programs import ProgramIn

programs_view = ModelView(
    model=Program,
    pydantic_model=ProgramIn,
    label="Programs",
)
