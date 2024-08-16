# mypy: disable-error-code="list-item"
from starlette_admin.contrib.sqla.ext.pydantic import ModelView

from apps.programs.models.further_tracks import FurtherTrack
from apps.programs.schemas.further_tracks import FurtherTrackIn


class FurtherTracksView(ModelView):
    exclude_fields_from_create = [FurtherTrack.statistics]


further_tracks_view = FurtherTracksView(
    model=FurtherTrack,
    pydantic_model=FurtherTrackIn,
    label="Further Tracks",
)
