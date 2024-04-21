from event.dto.book_event_request import BookEventRequest
from event.exception.event_not_exist_exception import EventNotExistException
from event.models import Event


class Events:
    def book_event(self, request: BookEventRequest):
        event = Event.objects.get(name=request.get_event_name())
        if event is None:
            raise EventNotExistException(f"{request.get_event_name()} doesn't exist ")

