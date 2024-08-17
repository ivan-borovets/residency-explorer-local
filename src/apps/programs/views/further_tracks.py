# mypy: disable-error-code="list-item"
from typing import Any, Dict

from starlette.requests import Request
from starlette_admin.contrib.sqla.ext.pydantic import ModelView

from apps.programs.models.further_tracks import FurtherTrack
from apps.programs.schemas.further_tracks import FurtherTrackIn
from apps.programs.views.error_handlers.integrity import handle_integrity_error


class FurtherTracksView(ModelView):
    exclude_fields_from_create = [FurtherTrack.statistics]

    @handle_integrity_error(schema=FurtherTrackIn)
    async def create(self, request: Request, data: Dict[str, Any]) -> Any:
        return await super().create(request, data)

    @handle_integrity_error(schema=FurtherTrackIn)
    async def edit(self, request: Request, pk: Any, data: Dict[str, Any]) -> Any:
        return await super().edit(request, pk, data)


further_tracks_view = FurtherTracksView(
    model=FurtherTrack,
    pydantic_model=FurtherTrackIn,
    label="Further Tracks",
)
