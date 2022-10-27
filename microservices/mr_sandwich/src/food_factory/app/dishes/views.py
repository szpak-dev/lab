from datetime import timedelta
from django.http import HttpResponse
from django.utils import timezone
from rest_framework.decorators import api_view

from dishes.errors import DishNotFound, DailyAvailabilityNotCreatedYet, DishBecameUnavailable, RevisionIsOutdated
from dishes.services import assert_daily_availability_exists, create_daily_availability, get_dish, reserve_dish, \
    get_daily_availability


def index(request):
    return HttpResponse('Hello from Food Factory Django')


@api_view(['GET', 'DELETE'])
def handle_reservation_action(request, dish_id: int, reservation_id: int):
    customer_id = 1
    if request.method == 'GET':
        return get_reservation(request, dish_id, customer_id)
    if request.method == 'DELETE':
        return remove_reservation(request, dish_id, customer_id)


def remove_reservation(request, dish_id: int, customer_id: int):
    return HttpResponse('Reservation removed')


def get_reservation(request, dish_id: int, customer_id: int):
    return HttpResponse('Your Reservation')


@api_view(['POST'])
def make_reservation(request, dish_id: int):
    tomorrow = timezone.now() + timedelta(days=1)
    print(request.POST, flush=True)
    customer_id = 1

    try:
        dish = get_dish(dish_id)
    except DishNotFound:
        return HttpResponse(
            status=404,
            content=b'There is no such Dish',
        )

    try:
        assert_daily_availability_exists(dish_id, tomorrow)
        daily_availability = get_daily_availability(dish_id, tomorrow)
    except DailyAvailabilityNotCreatedYet:
        create_daily_availability(dish_id, dish.daily_limit, tomorrow)
        daily_availability = get_daily_availability(dish_id, tomorrow)
    except DishBecameUnavailable:
        return HttpResponse(
            status=422,
            content=b'Dish is unavailable',
        )

    try:
        reserve_dish(daily_availability, customer_id)
    except RevisionIsOutdated:
        return HttpResponse(
            status=409,
            content=b'For some reason data became obsolete, please try again',
        )

    return HttpResponse(
        status=201,
        content=b'Reservation created',
    )
