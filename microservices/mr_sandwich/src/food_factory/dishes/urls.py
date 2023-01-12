from django.urls import path

from .actions.create_reservation.api import CreateReservationAPI
from .actions.get_reservation.api import GetReservationAPI
from .actions.remove_reservation.api import RemoveReservationAPI

urlpatterns = [
    path('reservations/', CreateReservationAPI.as_view()),
    path('reservations/customers/<int:customer_id>', GetReservationAPI.as_view()),
    path('reservations/<int:reservation_id>/', RemoveReservationAPI.as_view()),
]
