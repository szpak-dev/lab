from pydantic import BaseModel, Field


class NewReservation(BaseModel):
    """POST schema for reservation creation"""
    customer_id: int = Field(description='ID of the Customer')
    dish_id: int = Field(description='ID of the Dish')
