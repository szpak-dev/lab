from pydantic import BaseModel, Field

from dishes.actions import ErrorResponse


class Reservation(BaseModel):
    """Current Reservation of the Customer"""
    id: int = Field(description='Reservation Id')


class ReservationNotFoundResponse(ErrorResponse):
    """Reservation not found"""
