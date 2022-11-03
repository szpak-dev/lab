from datetime import timedelta
from rest_framework.response import Response
from django.utils import timezone

import dishes.services as services
from .requests import NewReservation

from dishes.errors import (
    DishNotFound,
    DailyAvailabilityNotCreatedYet,
    DishBecameUnavailable,
    RevisionIsOutdated,
)


class CreateReservationAction:
    @staticmethod
    def handle(new_reservation: NewReservation) -> Response:
        tomorrow = timezone.now() + timedelta(days=1)
        customer_id, dish_id = new_reservation.customer_id, new_reservation.dish_id

        try:
            dish = services.get_dish(dish_id)
        except DishNotFound:
            return Response(
                status=404,
                data='Dish not found',
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
                data='Dish became unavailable',
            )

        try:
            reservation = services.reserve_dish(daily_availability, customer_id)
        except RevisionIsOutdated:
            return Response(
                status=409,
                data='Revision is outdated',
            )

        return Response(
            status=201,
            data=reservation,
        )