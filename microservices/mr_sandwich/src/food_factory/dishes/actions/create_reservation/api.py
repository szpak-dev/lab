from rest_framework.request import Request
from rest_framework.views import APIView

from .action import CreateReservationAction
from .requests import NewReservation
from .responses import DishNotFoundResponse, RevisionIsOutdatedResponse, DishBecameUnavailableResponse, Reservation


class CreateReservationAPI(APIView):
    """Reserve given Dish for the Customer"""
    summary = 'Create new Reservation'
    post_request_schema = NewReservation
    response_schema = {
        '201': Reservation,
        '404': DishNotFoundResponse,
        '409': RevisionIsOutdatedResponse,
        '422': DishBecameUnavailableResponse,
    }

    def post(self, request: Request):
        return CreateReservationAction.handle(NewReservation(**request.data))
