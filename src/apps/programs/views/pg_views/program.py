from starlette.requests import Request
from starlette_admin import BooleanField, DecimalField, IntegerField, StringField
from starlette_admin.contrib.sqla import ModelView

from apps.programs.models.pg_views.program import ProgramPgView


class ProgramPgViewView(ModelView):
    fields = [
        StringField(name="code", label="Code"),
        StringField(name="title", label="Title"),
        StringField(name="city", label="City"),
        StringField(name="state", label="State"),
        StringField(name="region", label="Region"),
        IntegerField(name="rating", label="Rating"),
        DecimalField(name="percentage_non_us", label="% Non-US"),
        DecimalField(name="percentage_applicants_interviewed", label="% Appl. Int."),
        BooleanField(name="internship", label="Internship"),
        BooleanField(name="more_than_two_russians_interviewed", label=">2 Rus. Int."),
        StringField(name="d_name", label="D. Name"),
        StringField(name="d_specialty", label="D. Specialty"),
        StringField(name="d_home_country", label="D. Home Country"),
        StringField(name="further_tracks", label="Further Tracks"),
    ]

    # BaseModelView
    def can_create(self, request: Request) -> bool:
        """Permission for creating new Items. Return True by default"""
        return False

    # BaseModelView
    def can_edit(self, request: Request) -> bool:
        """Permission for editing Items. Return True by default"""
        return False

    # BaseModelView
    def can_delete(self, request: Request) -> bool:
        """Permission for deleting Items. Return True by default"""
        return False


program_pg_view_view = ProgramPgViewView(
    model=ProgramPgView,
    label="Program Overview",
)