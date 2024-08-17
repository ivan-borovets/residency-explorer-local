from functools import wraps
from typing import Type

from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from starlette_admin.exceptions import FormValidationError


def handle_integrity_error(schema: Type[BaseModel]):
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
