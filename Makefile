CHATBOT_MODEL_NAME=tinyswallow-1.5b-instruct-q5_k_m.gguf
WHISPER_MODEL_NAME=whisper.bin

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