from pydantic import BaseModel, Field

from dishes.actions import ErrorResponse


class Reservation(BaseModel):
    """Newly created Reservation"""
    id: int = Field(description='ID of the newly created Reservation')


class DishNotFoundResponse(ErrorResponse):
    """Dish not found"""


class RevisionIsOutdatedResponse(ErrorResponse):
    """Revision of Reservation mismatch, please try again"""


class DishBecameUnavailableResponse(ErrorResponse):
    """Dish not available, all Dishes reserved"""
