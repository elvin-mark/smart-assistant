CHATBOT_MODEL_NAME=gemma-3-270m-it-Q8_0.gguf
WHISPER_MODEL_NAME=ggml-base.bin
EMBEDDINGS_MODEL_NAME=all-MiniLM-L6-v2-Q8_0.gguf
KOKORO_TTS_MODEL_NAME=model_fp16.onnx

binaries:
	docker run -it -v ./backbone/utils:/app --name builder --entrypoint sh alpine /app/entrypoint.sh
	docker rm builder

docker-chatbot:
	docker build -t smart-assistant/chatbot -f backbone/chatbot/Dockerfile .

run-chatbot:
	docker run -it -v ${CHATBOT_MODEL}:/models/${CHATBOT_MODEL_NAME} -e MODEL_NAME=${CHATBOT_MODEL_NAME} -p 8181:8181 --name chatbot smart-assistant/chatbot

docker-speech-recognition:
	docker build -t smart-assistant/speech-recognition -f backbone/speech-recognition/Dockerfile .

run-speech-recognition:
	docker run -it -v ${SPEECH_RECOGNITION_MODEL}:/models/${WHISPER_MODEL_NAME} -e MODEL_NAME=${WHISPER_MODEL_NAME} -p 8080:8080 --name speech-recognition smart-assistant/speech-recognition

docker-embeddings:
	docker build -t smart-assistant/embeddings -f backbone/embeddings/Dockerfile .

run-embeddings:
	docker run -it -v ${EMBEDDINGS_MODEL}:/models/${EMBEDDINGS_MODEL_NAME} -e MODEL_NAME=${EMBEDDINGS_MODEL_NAME} -p 8282:8282 --name embeddings smart-assistant/embeddings

docker-text-to-speech:
	docker build -t smart-assistant/text-to-speech -f backbone/text-to-speech/Dockerfile .

run-text-to-speech:
	docker run -it -v ${KOKORO_TTS_MODEL}:/app/assets/${KOKORO_TTS_MODEL_NAME} -e MODEL_NAME=${KOKORO_TTS_MODEL_NAME} -p 8383:8383 --name text-to-speech smart-assistant/text-to-speech

run-server:
	python3 -m streamlit run server.py