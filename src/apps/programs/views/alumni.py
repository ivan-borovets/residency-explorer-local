from starlette_admin.contrib.sqla.ext.pydantic import ModelView

from apps.programs.models.alumni import Alumnus
from apps.programs.schemas.alumni import AlumniIn

alumni_view = ModelView(
    model=Alumnus,
    pydantic_model=AlumniIn,
    label="Directors' Alumni",
)

# in-place modification
fields_dict = {field.name: field for field in alumni_view.fields}
fields_dict["directors"].required = True
