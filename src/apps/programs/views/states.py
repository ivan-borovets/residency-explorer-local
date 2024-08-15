from starlette_admin.contrib.sqla.ext.pydantic import ModelView

from apps.programs.models.states import State
from apps.programs.schemas.states import StateIn

states_view = ModelView(
    model=State,
    pydantic_model=StateIn,
    label="States",
)
