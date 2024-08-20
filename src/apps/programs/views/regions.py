from typing import Any, Dict, List, Optional, Sequence, Union

from starlette.requests import Request
from starlette_admin import ExportType, HasMany, IntegerField, StringField
from starlette_admin.contrib.sqla.ext.pydantic import ModelView

from apps.programs.constants import STR_MIN_LEN
from apps.programs.models.regions import Region
from apps.programs.schemas.regions import RegionIn

from .error_handlers.integrity import handle_unique_violation


class RegionsView(ModelView):
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
            placeholder="Mountain",
        ),
        HasMany(
            # BaseField
            name="states",
            label="States",
            exclude_from_create=True,
            exclude_from_edit=True,
            # RelationField
            identity="state",
        ),
    ]

    # initial order
    fields_default_sort = ["title"]  # ascending

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
            order_by = ["title asc"]
        items = list(await super().find_all(request, skip, limit, where, order_by))
        return items

    @handle_unique_violation(schema=RegionIn)
    async def create(self, request: Request, data: Dict[str, Any]) -> Any:
        return await super().create(request, data)

    @handle_unique_violation(schema=RegionIn)
    async def edit(self, request: Request, pk: Any, data: Dict[str, Any]) -> Any:
        return await super().edit(request, pk, data)


regions_view = RegionsView(
    model=Region,
    pydantic_model=RegionIn,
    label="Regions",
)
