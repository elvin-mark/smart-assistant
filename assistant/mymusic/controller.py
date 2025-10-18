from flask import Flask, request, jsonify
from mymusic.audio_player import AudioPlayer

def add_music_controllers(app: Flask, player: AudioPlayer = AudioPlayer(), prefix="/music"):
    @app.route(f"{prefix}/play", methods=["POST"])
    def play():
        data = request.json or {}
        path = data.get("path")
        index = data.get("index")
        if path:
            return jsonify(player.play_file(path))
        elif index is not None:
            return jsonify(player.play_index(int(index)))
        return jsonify({"error": "path or index required"}), 400

    @app.route(f"{prefix}/pause", methods=["POST"])
    def pause():
        return jsonify(player.pause())
    
    @app.route(f"{prefix}/resume", methods=["POST"])
    def resume():
        return jsonify(player.resume())

    @app.route(f"{prefix}/stop", methods=["POST"])
    def stop():
        return jsonify(player.stop())

    @app.route(f"{prefix}/next", methods=["POST"])
    def next_track():
        return jsonify(player.next())

    @app.route(f"{prefix}/previous", methods=["POST"])
    def previous_track():
        return jsonify(player.previous())

    @app.route(f"{prefix}/volume", methods=["POST"])
    def volume():
        data = request.json or {}
        vol = data.get("volume")
        if vol is None:
            return jsonify({"error": "volume required"}), 400
        return jsonify(player.set_volume(int(vol)))

    @app.route(f"{prefix}/status", methods=["GET"])
    def status():
        return jsonify(player.get_status())