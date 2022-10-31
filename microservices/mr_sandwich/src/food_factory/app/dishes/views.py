from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
import logging

from .actions.create_reservation_action import CreateReservationAction, NewReservation
from .actions.get_reservation_action import Reservation


class CreateReservationAPI(APIView):
    post_summary = 'Create new Reservation'
    post_request_schema = NewReservation
    post_response_schema = Reservation

    def post(self, request: Request):
        # logging.warning(request.data)
        # logging.warning(NewReservation(**request.data))
        CreateReservationAction.handle(NewReservation(**request.data))
        return Response({})


class GetReservationAPI(APIView):
    post_response_schema = Reservation

    def get(self, request):
        pass


class RemoveReservationAPI(APIView):
    def delete(self, request):
        pass
