# mypy: disable-error-code="list-item"
from starlette_admin.contrib.sqla.ext.pydantic import ModelView

from apps.programs.models.states import State
from apps.programs.schemas.states import StateIn


class StatesView(ModelView):
    exclude_fields_from_create = [State.programs]


states_view = StatesView(
    model=State,
    pydantic_model=StateIn,
    label="States & Regions",
)
