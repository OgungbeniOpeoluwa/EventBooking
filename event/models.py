from uuid import uuid4

from django.db import models
from fast_booking import settings


# Create your models here.

class Event(models.Model):
    EVENT_CHOICE = [
        ("CONFERENCE", "CF"),
        ("GAME", "GA"),
        ("CONCERT", "CT"),
    ]
    name = models.CharField(max_length=100)
    date = models.DateField()
    available_attendee_count = models.IntegerField()
    event_description = models.CharField(max_length=500)
    category = models.CharField(choices=EVENT_CHOICE, max_length=20)
    booked_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='booked_event')
    organizer = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='organizer_event')

    def __str__(self):
        return self.name


class Ticket(models.Model):
    TICKET_CHOICE = [
        ("CONFIRMED", "C0"),
        ("CANCELLED", "CA"),
        ("EXPIRED", "EX"),
    ]
    ticket_id = models.UUIDField(default=uuid4)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    space_reserved = models.IntegerField()
    user_name = models.CharField(max_length=255)
    ticket_status = models.CharField(default="CF", choices=TICKET_CHOICE, max_length=20)

    def __str__(self):
        return self.ticket_id
