/app/bin/llama-server -m /models/$TTS_MODEL_NAME --host 0.0.0.0 --port 8020 & 
/app/bin/llama-server -m /models/$WAVTOKENZER_MODEL_NAME --host 0.0.0.0 --port 8021 --embeddings --pooling none