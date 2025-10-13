import os
import json
import tempfile
import numpy as np
from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import FileResponse
from onnxruntime import InferenceSession
from misaki.en import G2P
import scipy.io.wavfile as wavfile

# Init FastAPI app
app = FastAPI()

# Load static assets on startup
g2p = G2P(trf=False, british=True, fallback=None)
vocab = json.load(open("/app/assets/vocab.json"))
voices = np.fromfile("/app/assets/bf_alice.bin", dtype=np.float32).reshape(-1, 1, 256)
model_path = os.path.join(
    "onnx", f"/app/assets/{os.getenv('MODEL_NAME','model_fp16.onnx')}"
)
session = InferenceSession(model_path)


@app.post("/tts")
def generate_audio(text: str = Form(...)):
    if not text.strip():
        raise HTTPException(status_code=400, detail="Empty text input")

    try:
        phonemes, _ = g2p(text)
        tokens = [vocab[p] for p in phonemes if p in vocab]

        if len(tokens) > 510:
            raise HTTPException(status_code=400, detail="Input too long")

        ref_s = voices[len(tokens)]
        input_tokens = [[0, *tokens, 0]]

        audio = session.run(
            None,
            {
                "input_ids": input_tokens,
                "style": ref_s,
                "speed": np.ones(1, dtype=np.float32),
            },
        )[0]

        # Write to temp WAV file
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            wavfile.write(tmp.name, 24000, audio[0])
            return FileResponse(tmp.name, media_type="audio/wav", filename="output.wav")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"TTS generation failed: {e}")
