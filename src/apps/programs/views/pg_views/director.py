from starlette.requests import Request
from starlette_admin import ExportType, IntegerField, StringField
from starlette_admin.contrib.sqla import ModelView

from apps.programs.models.pg_views.director import DirectorPgView


class DirectorPgViewView(ModelView):
    fields = [
        StringField(name="code", label="Program Code"),
        StringField(name="name", label="Name"),
        StringField(name="contact", label="Contact"),
        StringField(name="specialty", label="Specialty"),
        StringField(name="home_country", label="Home Country"),
        StringField(name="info", label="Info"),
        IntegerField(name="n_peers", label="N Peers"),
        IntegerField(name="n_alumni", label="N Alumni"),
    ]

    # initial order
    fields_default_sort = ["name"]  # ascending

    export_types = [
        ExportType.CSV,
        ExportType.EXCEL,
        ExportType.PDF,
        ExportType.PRINT,
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


director_pg_view_view = DirectorPgViewView(
    model=DirectorPgView,
    label="Director Overview",
)
