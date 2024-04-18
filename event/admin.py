from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', "event_description", "date", 'list_of_user', "category", 'organizer']


@admin.register(models.Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ["ticket_id", "space_reserved", "ticket_status", "event_name", "user_name"]
