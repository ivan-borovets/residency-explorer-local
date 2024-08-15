from starlette_admin.contrib.sqla import Admin, ModelView

from apps.programs.models.alumni import Alumnus
from apps.programs.models.directors import Director

# isort:skip  # pylint: disable=unused-import
from apps.programs.models.directors_alumni import DirectorsAlumnus  # noqa: F401

# isort:skip  # pylint: disable=unused-import
from apps.programs.models.directors_peers import DirectorsPeer  # noqa: F401
from apps.programs.models.peers import Peer
from apps.programs.models.program_statistics import ProgramStatistics
from apps.programs.models.programs import Program
from apps.programs.models.states import State
from core.databases.helper import db_helper

engine = db_helper.engine

admin = Admin(
    engine=engine,
    title="Residency Explorer",
    base_url="/",
)

admin.add_view(ModelView(Program))
admin.add_view(ModelView(State))
admin.add_view(ModelView(Director))
admin.add_view(ModelView(ProgramStatistics))
admin.add_view(ModelView(Peer))
admin.add_view(ModelView(Alumnus))
