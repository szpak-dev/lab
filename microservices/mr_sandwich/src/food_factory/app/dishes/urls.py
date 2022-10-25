from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reservations/<int:dish_id>/<int:customer_id>', views.make_reservation),
]
