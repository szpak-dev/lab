from rest_framework.views import APIView

from dishes.actions import EmptyResponse
from dishes.actions.remove_reservation.action import RemoveReservationAction
from dishes.actions.remove_reservation.requests import RemoveReservationParams
from dishes.actions.remove_reservation.responses import ReservationNotFoundResponse


class RemoveReservationAPI(APIView):
    """Cancel Reservation when Customer removes Dish form the Cart"""
    summary = 'Cancel Reservation'
    path_params = RemoveReservationParams
    response_schema = {
        '204': EmptyResponse,
        '404': ReservationNotFoundResponse,
    }

    def delete(self, request, reservation_id: int):
        return RemoveReservationAction.handle(reservation_id)
