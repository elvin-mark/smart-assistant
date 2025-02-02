CHATBOT_MODEL_NAME=tinyswallow-1.5b-instruct-q5_k_m.gguf
WHISPER_MODEL_NAME=whisper.bin
EMBEDDINGS_MODEL_NAME=all-MiniLM-L6-v2-Q8_0.gguf

binaries:
	docker run -it -v ./utils:/app --name builder --entrypoint sh alpine /app/entrypoint.sh
	docker rm builder

docker-chatbot:
	docker build -t smart-assistant/chatbot -f chatbot/Dockerfile .

run-chatbot:
	docker run -it -v ${CHATBOT_MODEL}:/models/${CHATBOT_MODEL_NAME} -e MODEL_NAME=${CHATBOT_MODEL_NAME} -p 8181:8181 --name chatbot smart-assistant/chatbot

docker-speech-recognition:
	docker build -t smart-assistant/speech-recognition -f speech-recognition/Dockerfile .

run-speech-recognition:
	docker run -it -v ${SPEECH_RECOGNITION_MODEL}:/models/${WHISPER_MODEL_NAME} -e MODEL_NAME=${WHISPER_MODEL_NAME} -p 8080:8080 --name speech-recognition smart-assistant/speech-recognition

docker-embeddings:
	docker build -t smart-assistant/embeddings -f embeddings/Dockerfile .

run-embeddings:
	docker run -it -v ${EMBEDDINGS_MODEL}:/models/${EMBEDDINGS_MODEL_NAME} -e MODEL_NAME=${EMBEDDINGS_MODEL_NAME} -p 8282:8282 --name embeddings smart-assistant/embeddings

docker-text-to-speech:
	docker build -t smart-assistant/text-to-speech -f text-to-speech/Dockerfile .

run-text-to-speech:
	docker run -it -v ${TTS_MODEL}:/models/${TTS_MODEL_NAME} -v ${WAVTOKENIZER_MODEL}:/models/${WAVTOKENIZER_MODEL_NAME} -e TTS_MODEL_NAME=${TTS_MODEL_NAME} -e WAVTOKENIZER_MODEL_NAME=${WAVTOKENIZER_MODEL_NAME} -p 8020:8020 -p 8021:8021 --name text-to-speech smart-assistant/text-to-speech

run-server:
	python3 -m streamlit run server.py