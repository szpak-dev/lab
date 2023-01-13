from django.urls import path
from ninja import NinjaAPI
from ninja.responses import codes_4xx

from app.schema import Error
from dishes.errors import DishNotFound, DishBecameUnavailable, RevisionIsOutdated, ReservationNotFound
from dishes.use_cases.create_reservation.action import create_reservation_action
from dishes.use_cases.create_reservation.schemas import NewReservation, ReservationParams
from dishes.use_cases.get_reservation.action import get_reservation_action
from dishes.use_cases.get_reservation.schemas import Reservation
from dishes.use_cases.remove_reservation.action import remove_reservation_action

api = NinjaAPI()


@api.post('/', response={
    201: NewReservation,
    codes_4xx: Error,
})
def create_reservation(request, data: ReservationParams):
    try:
        return create_reservation_action(data)
    except DishNotFound:
        return 404, {'message': 'Dish not found'}
    except DishBecameUnavailable:
        return 422, {'message': 'Dish became unavailable'}
    except RevisionIsOutdated:
        return 409, {'message': 'Revision is outdated'}


@api.get('{int:reservation_id}/customers/{int:customer_id}', response={
    200: Reservation,
    codes_4xx: Error,
})
def get_reservation(request, reservation_id: int, customer_id: int):
    try:
        return get_reservation_action(reservation_id, customer_id)
    except ReservationNotFound:
        return 404, {'message': 'Reservation not found'}


@api.delete('/{int:reservation_id}', response={
    204: None,
    codes_4xx: Error,
})
def remove_reservation(request, reservation_id: int):
    try:
        remove_reservation_action(reservation_id)
        return 204, None
    except ReservationNotFound:
        return 404, {'message': 'Reservation not found'}


urlpatterns = [
    path('reservations/', api.urls),
]