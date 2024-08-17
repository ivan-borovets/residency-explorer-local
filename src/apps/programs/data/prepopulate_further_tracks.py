from dataclasses import dataclass

from sqlalchemy.orm import Session

from apps.programs.models.further_tracks import FurtherTrack


@dataclass
class FurtherTrackData:
    title: str


further_tracks_data = [
    FurtherTrackData(title="academic"),
    FurtherTrackData(title="full-time"),
    FurtherTrackData(title="residency"),
    FurtherTrackData(title="other"),
]


def prepopulate_further_tracks(session: Session):
    for further_track_data in further_tracks_data:
        further_track = FurtherTrack(title=further_track_data.title)
        session.add(further_track)
    session.commit()
