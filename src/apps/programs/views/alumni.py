from starlette_admin import (
    ExportType,
    HasMany,
    IntegerField,
    StringField,
    TextAreaField,
)
from starlette_admin.contrib.sqla.ext.pydantic import ModelView

from apps.programs.constants import STR_MIN_LEN
from apps.programs.models.alumni import Alumnus
from apps.programs.schemas.alumni import AlumniIn


class AlumniView(ModelView):
    fields = [
        IntegerField(
            # BaseField
            name="id",
            label="Id",
            exclude_from_list=True,
            exclude_from_detail=True,
        ),
        StringField(
            # BaseField
            name="first_name",
            label="First name",
            required=True,
            # StringField
            minlength=STR_MIN_LEN,
            placeholder="John",
        ),
        StringField(
            # BaseField
            name="last_name",
            label="Last name",
            required=True,
            # StringField
            minlength=STR_MIN_LEN,
            placeholder="Doe",
        ),
        TextAreaField(
            # BaseField
            name="contact_info",
            label="Contact info",
            required=True,
            # StringField
            minlength=STR_MIN_LEN,
            placeholder="+1 (555) 123-4567, "
            "john.doe@example.com, "
            "123 Main St, Springfield, IL",
        ),
        StringField(
            # BaseField
            name="work_location",
            label="Work location",
            # StringField
            minlength=STR_MIN_LEN,
            placeholder="St. Mary's Hospital, "
            "Cardiology Department, "
            "New York, NY",
        ),
        HasMany(
            # BaseField
            name="directors",
            label="Directors",
            required=True,
            # RelationField
            identity="director",
        ),
        TextAreaField(
            # BaseField
            name="additional_info",
            label="Additional info",
            # StringField
            minlength=STR_MIN_LEN,
            placeholder="The alumnus who loves cats",
        ),
    ]

    # initial order
    fields_default_sort = ["first_name"]  # ascending

    export_types = [
        ExportType.CSV,
        ExportType.EXCEL,
        ExportType.PDF,
        ExportType.PRINT,
    ]


alumni_view = AlumniView(
    model=Alumnus,
    pydantic_model=AlumniIn,
    label="Directors' Alumni",
)
