from rest_framework.response import Response

from dishes.actions.get_reservation.responses import Reservation


class GetReservationAction:
    @staticmethod
    def handle(customer_id: int) -> Response:
        return Response(
            status=200,
            data=Reservation(id=1)
        )
