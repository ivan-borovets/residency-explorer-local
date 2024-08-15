from starlette_admin.contrib.sqla.ext.pydantic import ModelView

from apps.programs.models.directors import Director
from apps.programs.schemas.directors import DirectorIn

directors_view = ModelView(
    model=Director,
    pydantic_model=DirectorIn,
    label="Directors",
)
