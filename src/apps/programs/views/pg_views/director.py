from starlette_admin import IntegerField, StringField
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


director_pg_view_view = DirectorPgViewView(
    model=DirectorPgView,
    label="Director Overview",
)
