from typing import Any, Dict, List, Optional, Sequence, Union

from starlette.requests import Request
from starlette_admin import (
    ExportType,
    HasMany,
    HasOne,
    IntegerField,
    StringField,
    TextAreaField,
)
from starlette_admin.contrib.sqla.ext.pydantic import ModelView

from apps.programs.constants import STR_MIN_LEN
from apps.programs.models.directors import Director
from apps.programs.schemas.directors import DirectorIn
from apps.programs.views.error_handlers.integrity import handle_not_null_violation


class DirectorsView(ModelView):
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
            name="first_name",
            label="First name",
            required=True,
            # StringField
            minlength=STR_MIN_LEN,
            placeholder="John",
        ),
        StringField(
            # BaseField
            name="last_name",
            label="Last name",
            required=True,
            # StringField
            minlength=STR_MIN_LEN,
            placeholder="Doe",
        ),
        TextAreaField(
            # BaseField
            name="contact_info",
            label="Contact info",
            required=True,
            # StringField
            minlength=STR_MIN_LEN,
            placeholder="+1 (555) 123-4567, "
            "john.doe@example.com, "
            "123 Main St, Springfield, IL",
        ),
        StringField(
            # BaseField
            name="specialty",
            label="Specialty",
            # StringField
            minlength=STR_MIN_LEN,
            placeholder="Cardiologist",
        ),
        StringField(
            # BaseField
            name="home_country",
            label="Home country",
            # StringField
            minlength=STR_MIN_LEN,
            placeholder="Netherlands",
        ),
        TextAreaField(
            # BaseField
            name="additional_info",
            label="Additional info",
            # StringField
            minlength=STR_MIN_LEN,
            placeholder="The director who loves cats",
        ),
        HasOne(
            # BaseField
            name="program",
            label="Program",
            required=True,
            # RelationField
            identity="program",
        ),
        HasMany(
            # BaseField
            name="alumni",
            label="Alumni",
            exclude_from_create=True,
            exclude_from_edit=True,
            # RelationField
            identity="alumnus",
        ),
        HasMany(
            # BaseField
            name="peers",
            label="Peers",
            exclude_from_create=True,
            exclude_from_edit=True,
            # RelationField
            identity="peer",
        ),
    ]

    # initial order
    fields_default_sort = ["first_name"]  # ascending

    export_types = [
        ExportType.CSV,
        ExportType.EXCEL,
        ExportType.PDF,
        ExportType.PRINT,
    ]

    # overridden for dropdown list sorting in forms
    async def find_all(
        self,
        request: Request,
        skip: int = 0,
        limit: int = 100,
        where: Union[Dict[str, Any], str, None] = None,
        order_by: Optional[List[str]] = None,
    ) -> Sequence[Any]:
        if request.query_params.get("select2"):
            order_by = ["first_name asc"]
        items = list(await super().find_all(request, skip, limit, where, order_by))
        return items

    @handle_not_null_violation(schema=DirectorIn)
    async def create(self, request: Request, data: Dict[str, Any]) -> Any:
        return await super().create(request, data)

    @handle_not_null_violation(schema=DirectorIn)
    async def edit(self, request: Request, pk: Any, data: Dict[str, Any]) -> Any:
        return await super().edit(request, pk, data)


directors_view = DirectorsView(
    model=Director,
    pydantic_model=DirectorIn,
    label="Directors",
)
