import os

LLM_TYPE = os.getenv("LLM_TYPE", "local")
LLM_ENDPOINT = "http://localhost:8181/v1"
LLM_API_KEY = "no-key"
EMBEDDINGS_ENDPOINT = "http://localhost:8282/embedding"
ASR_ENDPOINT = "http://localhost:8080/inference"
TTS_ENDPOINT = "http://localhost:8383/v1/audio/speech"

ASSISTANT_SERVER = "http://localhost:5100"