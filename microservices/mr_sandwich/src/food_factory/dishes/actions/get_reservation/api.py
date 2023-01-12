from rest_framework.views import APIView

from dishes.actions.get_reservation.action import GetReservationAction
from dishes.actions.get_reservation.requests import GetReservationParams
from dishes.actions.get_reservation.responses import Reservation, ReservationNotFoundResponse


class GetReservationAPI(APIView):
    """Allows fetching current Customer Reservation"""
    summary = 'Get current Reservation'
    path_params = GetReservationParams
    response_schema = {
        '200': Reservation,
        '404': ReservationNotFoundResponse,
    }

    def get(self, request, customer_id: int):
        return GetReservationAction.handle(customer_id)
