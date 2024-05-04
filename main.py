from flask import Flask, request, send_file
import numpy as np
from smart_assistant import SmartAssistant
import io
from scipy.io.wavfile import write as wav_write
import torch
import uuid
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
smart_assistant = SmartAssistant()
speech_map = {}

@app.route("/", methods=["GET"])
def home():
    return "home"


@app.route("/speech/recognition", methods=["GET"])
def speech_recognition():
    sampling_rate = request.args.get("sampling_rate", 16000)
    speech_audio = request.files.get("audio")
    buffer = speech_audio.stream.read()
    raw_data_buffer = np.frombuffer(buffer, dtype=np.int16).astype(np.float32)
    raw_data_buffer = raw_data_buffer / (2 ** 16 - 1)
    raw_data = torch.from_numpy(raw_data_buffer)
    transcription = smart_assistant.transcript(
        raw_data=raw_data, sampling_rate=sampling_rate)
    return {"result": transcription}


@app.route("/chatbot/response", methods=["GET"])
def chatbot_response():
    query = request.args.get("query")
    response = smart_assistant.chatbot_response(query,max_new_tokens=10)
    assistant_response = response.split("<|assistant|>")[1]
    return {"result": assistant_response}


@app.route("/speech/generation", methods=["GET"])
def speech_generation():
    query = request.args.get("query")
    speech = smart_assistant.generate_speech(query)
    bytes_wav = bytes()
    byte_io = io.BytesIO(bytes_wav)
    rate = 16000
    wav_write(byte_io, rate, (speech[0].numpy() *
              pow(2, 15)).astype(dtype=np.int16))
    return send_file(byte_io, as_attachment=True,download_name="speech.wav")

@app.route("/chatbot/converse", methods=["GET"])
def chatbot_converse():
    query = request.args.get("query","")
    raw_data = None
    if query == "":
        speech_audio = request.files.get("audio")
        buffer = speech_audio.stream.read()
        raw_data_buffer = np.frombuffer(buffer, dtype=np.int16).astype(np.float32)
        raw_data_buffer = raw_data_buffer / (2 ** 16 - 1)
        raw_data = torch.from_numpy(raw_data_buffer)
    response, response_audio = smart_assistant.converse(user_prompt=query,raw_data=raw_data,get_audio=True)
    id = str(uuid.uuid4())
    speech_map[id] = response_audio
    return {"result": response, "speech_id": id}

@app.route("/speech/from_map", methods=["GET"])
def speech_from_map():
    id = request.args.get("id")
    if id in speech_map:
        speech = speech_map[id]
        bytes_wav = bytes()
        byte_io = io.BytesIO(bytes_wav)
        rate = 16000
        wav_write(byte_io, rate, (speech[0].numpy() *
                pow(2, 15)).astype(dtype=np.int16))
        del speech_map[id]
        return send_file(byte_io, as_attachment=True,download_name="speech.wav")
    else:
        return {"error": "speech not found"}
if __name__ == "__main__":
    app.run()