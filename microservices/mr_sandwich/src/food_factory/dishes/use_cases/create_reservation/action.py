from datetime import timedelta
from django.utils import timezone

from dishes.models import DishReservation
from .schemas import ReservationParams
from dishes.services import Dishes, DailyAvailabilities, Reservations
from dishes.errors import DailyAvailabilityNotCreatedYet


def create_reservation_action(new_reservation: ReservationParams) -> DishReservation:
    tomorrow = timezone.now() + timedelta(days=1)
    customer_id, dish_id = new_reservation.customer_id, new_reservation.dish_id

    dish = Dishes.get_dish(dish_id)

    try:
        DailyAvailabilities.assert_daily_availability_exists(dish_id, tomorrow)
        daily_availability = DailyAvailabilities.get_daily_availability(dish_id, tomorrow)
    except DailyAvailabilityNotCreatedYet:
        DailyAvailabilities.create_daily_availability(dish_id, dish.daily_limit, tomorrow)
        daily_availability = DailyAvailabilities.get_daily_availability(dish_id, tomorrow)

    return Reservations.reserve_dish(daily_availability, customer_id)
