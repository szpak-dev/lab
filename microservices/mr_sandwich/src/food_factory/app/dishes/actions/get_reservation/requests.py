from pydantic import BaseModel, Field


class GetReservationParams(BaseModel):
    """Request path parameters"""
    customer_id: int = Field(description='Id of the currently logged Customer')
