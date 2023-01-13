from pydantic import BaseModel

from app.schema import ErrorResponse


class RemoveReservationParams(BaseModel):
    """Path parameters for removing given Reservation"""
    reservation_id: int


class ReservationNotFoundResponse(ErrorResponse):
    """Reservation not found"""
