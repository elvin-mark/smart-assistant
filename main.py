from flask import Flask, request, send_file
import numpy as np
from assistant import SmartAssistant
import io
from scipy.io.wavfile import write as wav_write

app = Flask(__name__)
smart_assistant = SmartAssistant()


@app.route("/", methods=["GET"])
def home():
    return "home"


@app.route("/speech/recognition", methods=["POST"])
def speech_recognition():
    sampling_rate = request.args.get("sampling_rate", 16000)
    speech_audio = request.files.get("audio")
    buffer = speech_audio.stream.read()
    raw_data_buffer = np.frombuffer(buffer, dtype=np.int16)
    transcription = smart_assistant.speech_recognition(
        raw_data_buffer, sampling_rate=sampling_rate)
    return {"result": transcription}


@app.route("/chatbot/response", methods=["GET"])
def chatbot_response():
    query = request.args.get("query")
    response = smart_assistant.chatbot_response(query)
    return {"result": response}


@app.route("/speech/generation", methods=["GET"])
def speech_generation():
    query = request.args.get("query")
    speech = smart_assistant.speech_generation(query)
    bytes_wav = bytes()
    byte_io = io.BytesIO(bytes_wav)
    rate = 16000
    wav_write(byte_io, rate, (speech.numpy() *
              pow(2, 15)).astype(dtype=np.int16))
    return send_file(byte_io, attachment_filename="speech.wav")


if __name__ == "__main__":
    app.run()
