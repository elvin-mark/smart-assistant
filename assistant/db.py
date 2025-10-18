from config import DB_PATH
import sqlite3


def init_db():
    """Create the events table if it doesn’t exist."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT,
            description TEXT
        )
    """
    )
    conn.commit()

    conn.close()
