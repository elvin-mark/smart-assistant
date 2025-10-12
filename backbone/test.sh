CHATBOT_PORT=8181
EMBEDDINGS_PORT=8282
TTS_PORT=8383
ASR_PORT=8080

curl localhost:${CHATBOT_PORT}/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{"messages": [{"role": "user", "content": "Hello"}]}' | jq .

curl localhost:${EMBEDDINGS_PORT}/embeddings \
    -H "Content-Type: application/json" \
    -d '{"content": "Hello"}' | jq .

mkdir -p tmp
curl localhost:${TTS_PORT}/tts \
    -F "text=Hello" \
    -o tmp/spoken.wav

curl localhost:${ASR_PORT}/inference \
    -F "file=@backbone/utils/whisper.cpp/samples/jfk.mp3" | jq .