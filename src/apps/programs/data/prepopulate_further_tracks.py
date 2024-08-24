from dataclasses import dataclass

from sqlalchemy.orm import Session

from apps.programs.models.further_tracks import FurtherTrack


@dataclass
class FurtherTrackData:
    title: str


further_tracks_data = [
    FurtherTrackData(title="academic"),
    FurtherTrackData(title="practice"),
    FurtherTrackData(title="fellowship"),
    FurtherTrackData(title="other"),
]


def prepopulate_further_tracks(session: Session) -> None:
    further_tracks = [FurtherTrack(title=data.title) for data in further_tracks_data]
    session.add_all(further_tracks)
    session.commit()
