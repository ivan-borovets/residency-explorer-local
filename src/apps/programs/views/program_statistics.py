from typing import Any, Dict

from starlette.requests import Request
from starlette_admin import (
    BooleanField,
    DecimalField,
    HasMany,
    HasOne,
    IntegerField,
    TextAreaField,
)
from starlette_admin.contrib.sqla.ext.pydantic import ModelView

from apps.programs.constants import STR_MIN_LEN
from apps.programs.models.program_statistics import ProgramStatistics
from apps.programs.schemas.program_statistics import ProgramStatisticsIn
from apps.programs.views.error_handlers.integrity import handle_not_null_violation


class ProgramStatisticsView(ModelView):
    fields = [
        IntegerField(
            # BaseField
            name="id",
            label="Id",
            exclude_from_list=True,
            exclude_from_detail=True,
        ),
        DecimalField(
            # BaseField
            name="percentage_non_us_img",
            label="% non-US IMG",
            help_text="0.00 - 100.00",
            required=True,
        ),
        DecimalField(
            # BaseField
            name="percentage_applicants_interviewed",
            label="% applicants interviewed",
            help_text="0.00 - 100.00",
        ),
        BooleanField(
            # BaseField
            name="internship_available",
            label="Internship available",
        ),
        BooleanField(
            # BaseField
            name="more_than_two_russians_interviewed",
            label=">2 russians interviewed",
        ),
        TextAreaField(
            # BaseField
            name="additional_info",
            label="Additional info",
            # StringField
            minlength=STR_MIN_LEN,
            placeholder="Cat lovers",
        ),
        HasOne(
            # BaseField
            name="program",
            label="Program",
            required=True,
            # RelationField
            identity="program",
        ),
        HasMany(
            # BaseField
            name="further_tracks",
            label="Further tracks",
            # RelationField
            identity="further-track",
        ),
    ]

    # initial order
    fields_default_sort = [
        ("percentage_non_us_img", True),  # descending
        ("percentage_applicants_interviewed", True),
    ]

    @handle_not_null_violation(schema=ProgramStatisticsIn)
    async def create(self, request: Request, data: Dict[str, Any]) -> Any:
        return await super().create(request, data)

    @handle_not_null_violation(schema=ProgramStatisticsIn)
    async def edit(self, request: Request, pk: Any, data: Dict[str, Any]) -> Any:
        return await super().edit(request, pk, data)


program_statistics_view = ProgramStatisticsView(
    model=ProgramStatistics,
    pydantic_model=ProgramStatisticsIn,
    label="Program Statistics",
)
