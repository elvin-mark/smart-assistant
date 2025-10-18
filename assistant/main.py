from flask import Flask
from mymusic import add_music_controllers
from mycalendar import add_calendar_controllers
from db import init_db

app = Flask(__name__)
init_db()

add_music_controllers(app)
add_calendar_controllers(app)

if __name__ == "__main__":
    print("Assistant server running on http://127.0.0.1:5100")
    app.run(host="127.0.0.1", port=5100)
