import vlc
import threading
import time
import os


class AudioPlayer:
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.playlist = []
        self.current_index = -1
        self.lock = threading.RLock()

    def _play(self, path):
        media = self.instance.media_new(path)
        self.player.set_media(media)
        self.player.play()
        time.sleep(0.1)

    def play_file(self, path):
        with self.lock:
            if not os.path.exists(path):
                return {"error": f"File not found: {path}"}
            if path not in self.playlist:
                self.playlist.append(path)
                self.current_index = len(self.playlist) - 1
            self._play(path)
            return {"status": "playing", "path": path}

    def play_index(self, index):
        with self.lock:
            if index < 0 or index >= len(self.playlist):
                return {"error": "index out of range"}
            self.current_index = index
            path = self.playlist[index]
            self._play(path)
            return {"status": "playing", "path": path}

    def pause(self):
        with self.lock:
            self.player.get_state()
            if self.player.is_playing():
                self.player.pause()
            return {"status": "paused"}
        
    def resume(self):
        with self.lock:
            self.player.get_state()
            if not self.player.is_playing():
                self.player.pause()
            return {"status": "resumed"}

    def stop(self):
        with self.lock:
            self.player.stop()
            return {"status": "stopped"}

    def next(self):
        with self.lock:
            if self.current_index + 1 < len(self.playlist):
                self.current_index += 1
                self._play(self.playlist[self.current_index])
                return {"status": "next", "path": self.playlist[self.current_index]}
            return {"status": "end_of_playlist"}

    def previous(self):
        with self.lock:
            if self.current_index > 0:
                self.current_index -= 1
                self._play(self.playlist[self.current_index])
                return {"status": "previous", "path": self.playlist[self.current_index]}
            return {"status": "start_of_playlist"}

    def set_volume(self, vol: int):
        vol = max(0, min(vol, 100))
        self.player.audio_set_volume(vol)
        return {"status": "ok", "volume": vol}

    def get_status(self):
        with self.lock:
            pos = self.player.get_position()
            vol = self.player.audio_get_volume()
            length = self.player.get_length() / 1000
            time_ms = self.player.get_time() / 1000
            state = str(self.player.get_state())
            current_path = self.playlist[self.current_index] if self.current_index >= 0 else None
            return {
                "state": state,
                "position": pos,
                "time_s": time_ms,
                "length_s": length,
                "volume": vol,
                "current": current_path,
                "playlist": self.playlist,
                "index": self.current_index
            }
