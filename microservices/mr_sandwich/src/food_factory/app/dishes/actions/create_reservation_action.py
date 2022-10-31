from datetime import timedelta
from pydantic import BaseModel, Field
from rest_framework.response import Response
from djantic import ModelSchema
from django.utils import timezone
import dishes.services as services

from dishes.errors import (
    DishNotFound,
    DailyAvailabilityNotCreatedYet,
    DishBecameUnavailable,
    RevisionIsOutdated,
)


class NewReservation(BaseModel):
    """POST schema for reservation creation"""
    customer_id: int = Field(description='ID of the Customer')
    dish_id: int = Field(description='ID of the Dish')


class CreateReservationAction:
    @staticmethod
    def handle(new_reservation: NewReservation):
        tomorrow = timezone.now() + timedelta(days=1)
        customer_id, dish_id = new_reservation.customer_id, new_reservation.dish_id

        try:
            dish = services.get_dish(dish_id)
        except DishNotFound:
            return Response(
                status=404,
            )

        try:
            services.assert_daily_availability_exists(dish_id, tomorrow)
            daily_availability = services.get_daily_availability(dish_id, tomorrow)
        except DailyAvailabilityNotCreatedYet:
            services.create_daily_availability(dish_id, dish.daily_limit, tomorrow)
            daily_availability = services.get_daily_availability(dish_id, tomorrow)
        except DishBecameUnavailable:
            return Response(
                status=422,
            )

        try:
            services.reserve_dish(daily_availability, customer_id)
        except RevisionIsOutdated:
            return Response(
                status=409,
            )

        return Response(
            status=201,
        )
