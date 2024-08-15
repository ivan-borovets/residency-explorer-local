from starlette_admin.contrib.sqla import Admin

# pylint: disable=unused-import
import boilerplate_model_imports  # noqa: F401
from apps.programs.views.alumni import alumni_view
from apps.programs.views.directors import directors_view
from apps.programs.views.peers import peers_view
from apps.programs.views.program_statistics import program_statistics_view
from apps.programs.views.programs import programs_view
from apps.programs.views.states import states_view
from core.databases.helper import db_helper

engine = db_helper.engine

admin = Admin(
    engine=engine,
    title="Residency Explorer",
    base_url="/",
)

views = (
    alumni_view,
    directors_view,
    peers_view,
    program_statistics_view,
    programs_view,
    states_view,
)

for view in views:
    admin.add_view(view)
