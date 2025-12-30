from langchain.tools import tool
import requests
from pydantic import BaseModel
from typing import Optional, Union
from datetime import datetime
from engine.config import ASSISTANT_SERVER

CALENDAR_SERVER = f"{ASSISTANT_SERVER}/calendar"


class Event(BaseModel):
    id: Optional[int] = None
    title: str
    date: str           # YYYY-MM-DD
    time: Optional[str] = None
    description: Optional[str] = None

@tool("get_today_date")
def get_today_date(dummy: str):
    """Get the current date in the format YYYY-MM-DD. Do not guess today's date, instead use this tool to get the proper date"""
    try:
        res = datetime.now().strftime("%Y-%m-%d")
        return res
    except Exception as e:
        return f"Error getting today's date: {str(e)}"



@tool("calendar_add_event")
def calendar_add_event(event: Union[Event, str]) -> str:
    """Add a new event. Input must be a Pydantic Event object."""
    try:
        if type(event) == str:
            event = Event.parse_raw(event)
        print(event.model_dump())
        res = requests.post(f"{CALENDAR_SERVER}/add_event", json=event.model_dump())
        return res.text
    except Exception as e:
        return f"Error adding event: {str(e)}"


@tool("calendar_list_events")
def calendar_list_events(dummy: str) -> str:
    """List all events in the calendar."""
    try:
        res = requests.get(f"{CALENDAR_SERVER}/list_events")
        return res.text
    except Exception as e:
        return f"Error listing events: {str(e)}"


@tool("calendar_get_event")
def calendar_get_event(event_id: str) -> str:
    """Get a specific event by ID."""
    try:
        res = requests.get(f"{CALENDAR_SERVER}/get_event", params={"id": event_id})
        return res.text
    except Exception as e:
        return f"Error fetching event: {str(e)}"


@tool("calendar_update_event")
def calendar_update_event(event: Union[Event, str]) -> str:
    """Update an existing event by ID using a Pydantic Event object."""
    try:
        if type(event) == str:
            event = Event.parse_raw(event)
        original_event = requests.get(f"{CALENDAR_SERVER}/get_event", params={"id": event.id})
        if original_event.status_code == 404:
            return f"Event with ID {event.id} not found"
        original_event = original_event.json()
        if event.title is None:
            event.title = original_event["title"]
        if event.date is None:
            event.date = original_event["date"]
        if event.time is None:
            event.time = original_event["time"]
        if event.description is None:
            event.description = original_event["description"]
        payload = event.dict()
        payload["id"] = event.id
        res = requests.post(f"{CALENDAR_SERVER}/update_event", json=payload)
        return res.text
    except Exception as e:
        return f"Error updating event: {str(e)}"


@tool("calendar_delete_event")
def calendar_delete_event(event_id: str) -> str:
    """Delete an event by ID."""
    try:
        res = requests.post(f"{CALENDAR_SERVER}/delete_event", json={"id": event_id})
        return res.text
    except Exception as e:
        return f"Error deleting event: {str(e)}"


@tool("calendar_events_on_date")
def calendar_events_on_date(date: str) -> str:
    """Get all events for a specific date (YYYY-MM-DD)."""
    try:
        res = requests.get(f"{CALENDAR_SERVER}/events_on_date", params={"date": date})
        return res.text
    except Exception as e:
        return f"Error fetching events: {str(e)}"