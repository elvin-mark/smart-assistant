import sqlite3

from mycalendar.repository import MyCalendarRepository


class MyCalendarService:
    def __init__(self, repository: MyCalendarRepository):
        self.repository = repository

    def add_event(
        self, title: str, date: str, time: str = None, description: str = ""
    ) -> int:
        """Add a new event and return its ID."""
        return self.repository.add_event(title, date, time, description)

    def list_events(self) -> list:
        """Return all events."""
        return self.repository.list_events()

    def get_event(self, event_id: int) -> dict | None:
        """Fetch a single event by ID."""
        return self.repository.get_event(event_id)

    def update_event(
        self, event_id: int, title=None, date=None, time=None, description=None
    ) -> bool:
        """Update fields of an existing event."""
        return self.repository.update_event(event_id, title, date, time, description)

    def delete_event(self, event_id: int) -> bool:
        """Delete an event by ID."""
        return self.repository.delete_event(event_id)

    def get_events_on_date(self, date: str) -> list:
        """Return all events on a specific date."""
        return self.repository.get_events_on_date(date)
