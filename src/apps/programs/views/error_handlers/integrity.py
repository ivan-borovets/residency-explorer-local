from functools import wraps
from typing import Any, Type

from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from starlette_admin.exceptions import FormValidationError


def handle_unique_violation(schema: Type[BaseModel]):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except IntegrityError as e:
                for field in schema.model_fields.keys():
                    if field in str(e.orig):
                        raise FormValidationError(
                            {field: f"An item with this {field} already exists."}
                        ) from e
                raise FormValidationError(
                    {"non_field_errors": "An integrity error occurred."}
                ) from e

        return wrapper

    return decorator


def handle_not_null_violation(schema: Type[BaseModel]):
    def decorator(func):
        @wraps(func)
        async def wrapper(view_instance: Any, *args, **kwargs):
            try:
                return await func(view_instance, *args, **kwargs)
            except IntegrityError as e:
                error_message = str(e.orig)
                if "violates not-null" in error_message:
                    label = getattr(
                        view_instance,
                        "label",
                        schema.__name__.replace("In", ""),
                    )
                    for field in schema.model_fields.keys():
                        if field in error_message:
                            raise FormValidationError(
                                {
                                    field: f"The specified {field.title()} is already "
                                    f"associated with the corresponding {label} data."
                                }
                            ) from e
                raise e

        return wrapper

    return decorator
