from pydantic import BaseModel, Field
from rest_framework.views import APIView
from rest_framework.response import Response


class Reservation(BaseModel):
    id: int = Field(description='Reservation Id')


class GetReservationAPI(APIView):
    response_schema = Reservation

    def get(self, request, customer_id: int):
        return Response(Reservation())
