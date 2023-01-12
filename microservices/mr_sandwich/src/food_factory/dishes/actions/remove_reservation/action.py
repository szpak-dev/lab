from rest_framework.response import Response


class RemoveReservationAction:
    @staticmethod
    def handle(reservation_id: int) -> Response:
        return Response(status=204)
