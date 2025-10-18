import sqlite3
from config import DB_PATH

class MyCalendarRepository:

    def __init__(self):
        pass

    def add_event(
        self, title: str, date: str, time: str = None, description: str = ""
    ) -> int:
        """Add a new event and return its ID."""
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO events (title, date, time, description) VALUES (?, ?, ?, ?)",
            (title, date, time, description),
        )
        conn.commit()
        conn.close()
        event_id = cur.lastrowid
        return event_id

    def list_events(self) -> list:
        """Return all events."""
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM events ORDER BY date, time")
        events = [dict(row) for row in cur.fetchall()]
        conn.close()
        return events

    def get_event(self, event_id: int) -> dict | None:
        """Fetch a single event by ID."""
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM events WHERE id = ?", (event_id,))
        event = cur.fetchone()
        conn.close()
        return dict(event) if event else None

    def update_event(
        self, event_id: int, title=None, date=None, time=None, description=None
    ) -> bool:
        """Update fields of an existing event."""
        fields = []
        values = []

        if title:
            fields.append("title = ?")
            values.append(title)
        if date:
            fields.append("date = ?")
            values.append(date)
        if time:
            fields.append("time = ?")
            values.append(time)
        if description:
            fields.append("description = ?")
            values.append(description)

        if not fields:
            return False

        values.append(event_id)
        query = f"UPDATE events SET {', '.join(fields)} WHERE id = ?"

        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query, tuple(values))
        conn.commit()
        updated = cur.rowcount > 0
        return updated

    def delete_event(self, event_id: int) -> bool:
        """Delete an event by ID."""
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("DELETE FROM events WHERE id = ?", (event_id,))
        conn.commit()
        deleted = cur.rowcount > 0
        conn.close()
        return deleted

    def get_events_on_date(self, date: str) -> list:
        """Return all events on a specific date."""
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM events WHERE date = ? ORDER BY time", (date,))
        events = [dict(row) for row in cur.fetchall()]
        return events
