from django.urls import path
from . import views

urlpatterns = [
    path("create_event/", views.create_event, name="create_event"),
    path("events/", views.event, name="event"),
    path("create_ticket/", views.create_ticket, name="create_ticket"),
]
