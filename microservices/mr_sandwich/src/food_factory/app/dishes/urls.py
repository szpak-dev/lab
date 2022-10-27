from django.urls import path

from . import views

urlpatterns = [
    path('reservations/<int:reservation_id>', views.handle_reservation_action),
    path('reservations/', views.make_reservation),
]
