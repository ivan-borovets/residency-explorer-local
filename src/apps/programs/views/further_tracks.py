from typing import Any, Dict, List, Optional, Sequence, Union

from starlette.requests import Request
from starlette_admin import ExportType, HasMany, IntegerField, StringField
from starlette_admin.contrib.sqla.ext.pydantic import ModelView

from apps.programs.constants import STR_MIN_LEN
from apps.programs.models.further_tracks import FurtherTrack
from apps.programs.schemas.further_tracks import FurtherTrackIn
from apps.programs.views.error_handlers.integrity import handle_unique_violation


class FurtherTracksView(ModelView):
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
            placeholder="residency",
        ),
        HasMany(
            # BaseField
            name="statistics",
            label="Statistics",
            exclude_from_create=True,
            exclude_from_edit=True,
            # RelationField
            identity="program-statistics",
        ),
    ]

    # initial order
    fields_default_sort = ["id"]  # ascending

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
            order_by = ["id asc"]
        items = list(await super().find_all(request, skip, limit, where, order_by))
        return items

    @handle_unique_violation(schema=FurtherTrackIn)
    async def create(self, request: Request, data: Dict[str, Any]) -> Any:
        return await super().create(request, data)

    @handle_unique_violation(schema=FurtherTrackIn)
    async def edit(self, request: Request, pk: Any, data: Dict[str, Any]) -> Any:
        return await super().edit(request, pk, data)


further_tracks_view = FurtherTracksView(
    model=FurtherTrack,
    pydantic_model=FurtherTrackIn,
    label="Further Tracks",
)
