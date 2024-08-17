from starlette_admin.contrib.sqla.ext.pydantic import ModelView

from apps.programs.models.program_statistics import ProgramStatistics
from apps.programs.schemas.program_statistics import ProgramStatisticsIn

program_statistics_view = ModelView(
    model=ProgramStatistics,
    pydantic_model=ProgramStatisticsIn,
    label="Program Statistics",
)

# in-place modification
fields_dict = {field.name: field for field in program_statistics_view.fields}
fields_dict["program"].required = True
fields_dict["further_tracks"].required = True