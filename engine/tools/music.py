from langchain.tools import tool
import requests
from engine.config import ASSISTANT_SERVER

MUSIC_SERVER = f"{ASSISTANT_SERVER}/music"


@tool("audio_play", return_direct=True)
def audio_play(song_name: str) -> str:
    """
    Play a specific song from the playlist.

    Args:
        song_name: Name of the song to play (must exist in the playlist).
    """
    try:
        res = requests.post(f"{MUSIC_SERVER}/play", data={"path": song_name})
        return res.text
    except Exception as e:
        return f"Error playing song: {str(e)}"


@tool("audio_stop", return_direct=True)
def audio_stop(dummy: str) -> str:
    """Stop the currently playing song."""
    try:
        res = requests.post(f"{MUSIC_SERVER}/stop")
        return res.text
    except Exception as e:
        return f"Error stopping audio: {str(e)}"


@tool("audio_pause", return_direct=True)
def audio_pause(dummy: str) -> str:
    """Pause the currently playing song."""
    try:
        res = requests.post(f"{MUSIC_SERVER}/pause")
        return res.text
    except Exception as e:
        return f"Error pausing audio: {str(e)}"


@tool("audio_resume", return_direct=True)
def audio_resume(dummy: str) -> str:
    """Resume playback of the paused song."""
    try:
        res = requests.post(f"{MUSIC_SERVER}/resume")
        return res.text
    except Exception as e:
        return f"Error resuming audio: {str(e)}"


@tool("audio_next", return_direct=True)
def audio_next(dummy: str) -> str:
    """Play the next song in the playlist."""
    try:
        res = requests.post(f"{MUSIC_SERVER}/next")
        return res.text
    except Exception as e:
        return f"Error skipping to next song: {str(e)}"


@tool("audio_previous", return_direct=True)
def audio_previous(dummy: str) -> str:
    """Play the previous song in the playlist."""
    try:
        res = requests.post(f"{MUSIC_SERVER}/previous")
        return res.text
    except Exception as e:
        return f"Error playing previous song: {str(e)}"


@tool("audio_status", return_direct=True)
def audio_status(dummy: str) -> str:
    """Get current playback status (song name, state, position)."""
    try:
        res = requests.get(f"{MUSIC_SERVER}/status")
        return res.text
    except Exception as e:
        return f"Error getting status: {str(e)}"
