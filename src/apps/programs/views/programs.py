from typing import Any, Dict

from starlette.requests import Request
from starlette_admin import HasOne, IntegerField, StringField
from starlette_admin.contrib.sqla.ext.pydantic import ModelView

from apps.programs.constants import STR_MIN_LEN
from apps.programs.models.programs import Program
from apps.programs.schemas.programs import ProgramIn
from apps.programs.views.error_handlers.integrity import handle_unique_violation


class ProgramsView(ModelView):
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
            name="code",
            label="NRMP program code",
            required=True,
            # StringField
            minlength=STR_MIN_LEN,
            placeholder="2335140C2",
        ),
        StringField(
            # BaseField
            name="title",
            label="Title",
            required=True,
            # StringField
            minlength=STR_MIN_LEN,
            placeholder="Northwest Healthcare Tucson’s Internal Medicine",
        ),
        StringField(
            # BaseField
            name="city",
            label="City",
            required=True,
            # StringField
            minlength=STR_MIN_LEN,
            placeholder="Tucson",
        ),
        HasOne(
            # BaseField
            name="state",
            label="State",
            required=True,
            # RelationField
            identity="state",
        ),
        IntegerField(
            # BaseField
            name="user_rating",
            label="My rating",
            help_text="1-5",
        ),
        HasOne(
            # BaseField
            name="director",
            label="Director",
            exclude_from_create=True,
            exclude_from_edit=True,
            # RelationField
            identity="director",
        ),
        HasOne(
            # BaseField
            name="statistics",
            label="Statistics",
            exclude_from_create=True,
            exclude_from_edit=True,
            # RelationField
            identity="program-statistics",
        ),
    ]

    @handle_unique_violation(schema=ProgramIn)
    async def create(self, request: Request, data: Dict[str, Any]) -> Any:
        return await super().create(request, data)

    @handle_unique_violation(schema=ProgramIn)
    async def edit(self, request: Request, pk: Any, data: Dict[str, Any]) -> Any:
        return await super().edit(request, pk, data)


programs_view = ProgramsView(
    model=Program,
    pydantic_model=ProgramIn,
    label="Programs",
)
