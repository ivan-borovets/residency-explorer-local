from dataclasses import dataclass

from sqlalchemy.orm import Session

from apps.programs.models.majors import Major


@dataclass
class MajorData:
    title: str


majors_data = [
    MajorData(title="Internal Medicine"),
    MajorData(title="Family Medicine"),
]


def prepopulate_majors(session: Session):
    for major_data in majors_data:
        major = Major(title=major_data.title)
        session.add(major)
    session.commit()
