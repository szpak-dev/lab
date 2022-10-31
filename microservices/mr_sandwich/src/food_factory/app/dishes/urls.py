from django.urls import path

from . import views

urlpatterns = [
    path('reservations/', views.CreateReservationAPI.as_view()),
    path('reservations/<int:reservation_id>', views.GetReservationAPI.as_view()),
    path('reservations/<int:reservation_id>/customers/<int:customer_id>', views.RemoveReservationAPI.as_view()),
]
