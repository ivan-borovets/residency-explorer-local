from typing import Any, Dict

from starlette.requests import Request
from starlette_admin import HasMany, HasOne, IntegerField, StringField
from starlette_admin.contrib.sqla.ext.pydantic import ModelView

from apps.programs.constants import STR_MIN_LEN
from apps.programs.models.states import State
from apps.programs.schemas.states import StateIn

from .error_handlers.integrity import handle_unique_violation


class StatesView(ModelView):
    fields = [
        IntegerField(
            # BaseField
            name="id",
            label="Id",
            exclude_from_list=True,
            exclude_from_detail=True,
        ),
        StringField(
            # BaseField
            name="title",
            label="Title",
            required=True,
            # StringField
            minlength=STR_MIN_LEN,
            placeholder="Nevada",
        ),
        HasOne(
            # BaseField
            name="region",
            label="Region",
            required=True,
            # RelationField
            identity="region",
        ),
        HasMany(
            # BaseField
            name="programs",
            label="Programs",
            exclude_from_create=True,
            exclude_from_edit=True,
            # RelationField
            identity="program",
        ),
    ]

    @handle_unique_violation(schema=StateIn)
    async def create(self, request: Request, data: Dict[str, Any]) -> Any:
        return await super().create(request, data)

    @handle_unique_violation(schema=StateIn)
    async def edit(self, request: Request, pk: Any, data: Dict[str, Any]) -> Any:
        return await super().edit(request, pk, data)


states_view = StatesView(
    model=State,
    pydantic_model=StateIn,
    label="States",
)
