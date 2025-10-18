from flask import Flask, request, jsonify
from mycalendar import MyCalendarService, MyCalendarRepository


def add_calendar_controllers(app: Flask, prefix="/calendar"):
    repository = MyCalendarRepository()
    service = MyCalendarService(repository)

    @app.route(f"{prefix}/add_event", methods=["POST"])
    def add_event():
        title = request.json.get("title")
        date = request.json.get("date")
        time = request.json.get("time")
        description = request.json.get("description", "")

        if not title or not date:
            return jsonify({"error": "title and date are required"}), 400

        event_id = service.add_event(title, date, time, description)
        return jsonify({"message": "event added", "event_id": event_id})

    @app.route(f"{prefix}/list_events", methods=["GET"])
    def list_events():
        return jsonify(service.list_events())

    @app.route(f"{prefix}/get_event", methods=["GET"])
    def get_event():
        event_id = request.args.get("id")
        if not event_id:
            return jsonify({"error": "missing id"}), 400

        event = service.get_event(event_id)
        if not event:
            return jsonify({"error": "event not found"}), 404
        return jsonify(event)

    @app.route(f"{prefix}/update_event", methods=["POST"])
    def update_event():
        event_id = request.json.get("id")
        if not event_id:
            return jsonify({"error": "missing id"}), 400

        updated = service.update_event(
            event_id,
            request.json.get("title"),
            request.json.get("date"),
            request.json.get("time"),
            request.json.get("description"),
        )
        if not updated:
            return jsonify({"error": "event not found or nothing to update"}), 404
        return jsonify({"message": "event updated"})

    @app.route(f"{prefix}/delete_event", methods=["POST"])
    def delete_event():
        event_id = request.json.get("id")
        if not event_id:
            return jsonify({"error": "missing id"}), 400

        deleted = service.delete_event(event_id)
        if not deleted:
            return jsonify({"error": "event not found"}), 404
        return jsonify({"message": "event deleted"})

    @app.route(f"{prefix}/events_on_date", methods=["GET"])
    def events_on_date():
        date = request.args.get("date")
        if not date:
            return jsonify({"error": "missing date"}), 400

        events = service.get_events_on_date(date)
        return jsonify(events)
