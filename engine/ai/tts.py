import requests
from engine.config import TTS_ENDPOINT


def text_to_speech(text: str):
    res = requests.post(TTS_ENDPOINT, json={"input": text})
    with open("tmp/spoken.wav", "wb") as f:
        f.write(res.content)
