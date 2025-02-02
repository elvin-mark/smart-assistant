/app/bin/llama-server -m /models/$TTS_MODEL_NAME --host 0.0.0.0 --port 8020 & 
/app/bin/llama-server -m /models/$WAVTOKENIZER_MODEL_NAME --host 0.0.0.0 --port 8021 --embeddings --pooling none