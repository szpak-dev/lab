from pydantic import BaseModel, Field


class RemoveReservationParams(BaseModel):
    """Path parameters for removing given Reservation"""
    reservation_id: int = Field(description='Id of the reservation to remove')
