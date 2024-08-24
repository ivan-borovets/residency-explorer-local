from dataclasses import dataclass

from sqlalchemy.orm import Session

from apps.programs.models.regions import Region
from apps.programs.models.states import State


@dataclass
class StateData:
    title: str


@dataclass
class RegionData:
    title: str
    states: tuple[StateData, ...]


regions_data = (
    RegionData(
        title="East North Central",
        states=(
            StateData(title="Illinois"),
            StateData(title="Indiana"),
            StateData(title="Michigan"),
            StateData(title="Ohio"),
            StateData(title="Wisconsin"),
        ),
    ),
    RegionData(
        title="East South Central",
        states=(
            StateData(title="Alabama"),
            StateData(title="Kentucky"),
            StateData(title="Mississippi"),
            StateData(title="Tennessee"),
        ),
    ),
    RegionData(
        title="Middle Atlantic",
        states=(
            StateData(title="New Jersey"),
            StateData(title="New York"),
            StateData(title="Pennsylvania"),
        ),
    ),
    RegionData(
        title="Mountain",
        states=(
            StateData(title="Arizona"),
            StateData(title="Colorado"),
            StateData(title="Idaho"),
            StateData(title="Montana"),
            StateData(title="Nevada"),
            StateData(title="New Mexico"),
            StateData(title="Utah"),
            StateData(title="Wyoming"),
        ),
    ),
    RegionData(
        title="New England",
        states=(
            StateData(title="Connecticut"),
            StateData(title="Maine"),
            StateData(title="Massachusetts"),
            StateData(title="New Hampshire"),
            StateData(title="Rhode Island"),
            StateData(title="Vermont"),
        ),
    ),
    RegionData(
        title="Pacific",
        states=(
            StateData(title="Alaska"),
            StateData(title="California"),
            StateData(title="Hawaii"),
            StateData(title="Oregon"),
            StateData(title="Washington"),
        ),
    ),
    RegionData(
        title="South Atlantic",
        states=(
            StateData(title="Delaware"),
            StateData(title="Florida"),
            StateData(title="Georgia"),
            StateData(title="Maryland"),
            StateData(title="North Carolina"),
            StateData(title="South Carolina"),
            StateData(title="Virginia"),
            StateData(title="Washington, D.C."),
            StateData(title="West Virginia"),
        ),
    ),
    RegionData(
        title="West North Central",
        states=(
            StateData(title="Iowa"),
            StateData(title="Kansas"),
            StateData(title="Minnesota"),
            StateData(title="Missouri"),
            StateData(title="Nebraska"),
            StateData(title="North Dakota"),
            StateData(title="South Dakota"),
        ),
    ),
    RegionData(
        title="West South Central",
        states=(
            StateData(title="Arkansas"),
            StateData(title="Louisiana"),
            StateData(title="Oklahoma"),
            StateData(title="Texas"),
        ),
    ),
)


def prepopulate_regions_and_states(session: Session) -> None:
    regions = []
    for region_data in regions_data:
        region = Region(title=region_data.title)
        region.states = [
            State(title=state_data.title) for state_data in region_data.states
        ]
        regions.append(region)

    session.add_all(regions)
    session.commit()
