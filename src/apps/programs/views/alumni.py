from starlette_admin.contrib.sqla.ext.pydantic import ModelView

from apps.programs.models.alumni import Alumnus
from apps.programs.schemas.alumni import AlumniIn

alumni_view = ModelView(
    model=Alumnus,
    pydantic_model=AlumniIn,
    label="Alumni",
)
