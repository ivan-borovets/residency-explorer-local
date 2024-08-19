from starlette_admin import DropDown
from starlette_admin.contrib.sqla import Admin

# pylint: disable=unused-import
import boilerplate_model_imports  # noqa: F401
from apps.programs.views.alumni import alumni_view
from apps.programs.views.directors import directors_view
from apps.programs.views.further_tracks import further_tracks_view
from apps.programs.views.peers import peers_view
from apps.programs.views.pg_views.director import director_pg_view_view
from apps.programs.views.pg_views.program import program_pg_view_view
from apps.programs.views.program_statistics import program_statistics_view
from apps.programs.views.programs import programs_view
from apps.programs.views.regions import regions_view
from apps.programs.views.states import states_view
from core.databases.helper import db_helper

engine = db_helper.engine

admin = Admin(
    engine=engine,
    title="Residency Explorer",
    base_url="/",
)

overviews = (
    program_pg_view_view,
    director_pg_view_view,
)

for overview in overviews:
    admin.add_view(overview)

admin.add_view(
    DropDown(
        label="Predefined",
        views=[
            regions_view,
            states_view,
            further_tracks_view,
        ],
        always_open=False,
    )
)

primary_views = (
    programs_view,
    program_statistics_view,
    directors_view,
    peers_view,
    alumni_view,
)

for view in primary_views:
    admin.add_view(view)
