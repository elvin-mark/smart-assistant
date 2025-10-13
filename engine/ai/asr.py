from typing import Any
import requests
from engine.config import ASR_ENDPOINT


def speech_recognition(data: Any) -> str:
    res = requests.post(ASR_ENDPOINT, files={"file": ("audio.wav", data.read())})
    return res.json().get("text", "")
