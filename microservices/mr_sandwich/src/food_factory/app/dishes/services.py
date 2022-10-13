from dishes.errors import DailyAvailabilityNotCreatedYet, DishNotFound, RevisionIsOutdated, DishBecameUnavailable
from dishes.models import DishDailyAvailability, Dish
from dishes.models import DishReservation
from django.db import transaction
from django.db.models import F
from django.core.exceptions import ObjectDoesNotExist


def assert_daily_availability_exists(dish_id: int, day) -> bool:
    if DishDailyAvailability.objects.filter(dish_id=dish_id, day=day).count() == 0:
        raise DailyAvailabilityNotCreatedYet('Daily Availability not created for the given day')


def create_daily_availability(dish_id: int, daily_limit: int, day):
    daily_availability = DishDailyAvailability(dish_id=dish_id, available_count=daily_limit, day=day)
    daily_availability.save()


def get_daily_availability(dish_id: int, day) -> DishDailyAvailability:
    try:
        return DishDailyAvailability.objects.get(dish_id=dish_id, day=day, available_count__gt=0)
    except ObjectDoesNotExist:
        raise DishBecameUnavailable('Dish Daily Availability with available dishes was not found')


def get_dish(dish_id: int) -> Dish:
    try:
        return Dish.objects.get(pk=dish_id)
    except ObjectDoesNotExist:
        raise DishNotFound('Dish with given Id was not found')


def reserve_dish(dish_daily_availability: DishDailyAvailability, customer_id: int):
    pk = dish_daily_availability.pk
    dish_id = dish_daily_availability.dish.id
    day = dish_daily_availability.day
    revision = dish_daily_availability.revision

    with transaction.atomic():
        updated = DishDailyAvailability.objects.filter(pk=pk, day=day, available_count__gt=0, revision=revision).update(
            available_count=F('available_count')-1,
        )

        if updated == 1:
            DishReservation(dish_id=dish_id, customer_id=customer_id).save()
            return

        raise RevisionIsOutdated('Available Dishes count has changed')
