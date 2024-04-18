import datetime
from uuid import uuid4

from django.db import models
from django.utils import timezone

from fast_booking import settings


# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    available_attendee_count = models.IntegerField()
    event_description = models.CharField(max_length=500)
    category = models.CharField(max_length=35)
    booked_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='booked_event')
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='organizer_event')

    def __str__(self):
        return self.name

    def list_of_user(self):
        return [users for users in self.booked_user.all()]


class Ticket(models.Model):
    TICKET_CHOICE = [
        ("CONFIRMED", "C0"),
        ("CANCELLED", "CA"),
        ("EXPIRED", "EX"),
    ]
    ticket_id = models.CharField(max_length=5)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    space_reserved = models.IntegerField()
    user_name = models.CharField(max_length=255)
    ticket_status = models.CharField(default="CONFIRMED", choices=TICKET_CHOICE, max_length=20)

    def __str__(self):
        return self.ticket_id

    def event_name(self):
        return self.event.name
