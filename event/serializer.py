from rest_framework import serializers
from .models import Event, Ticket


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'date', 'available_attendee_count', 'event_description', 'category', 'organizer']


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['ticket_id', 'event', 'space_reserved', 'username', 'ticket_status']
        read_only = ['ticket_status']
