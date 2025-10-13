# Text-to-Speech

For the chatbot, the [KokoroTTS](https://github.com/hexgrad/kokoro) model is being used, since this model it is light weigth and already good enough for this project. On top of that, to make a simple and fast inference server, the [TTS.cpp](https://github.com/mmwillet/TTS.cpp) server and the [gguf model of KokoroTTS](https://huggingface.co/mmwillet2/Kokoro_GGUF/tree/main) is used.

Note: Make sure to download the gguf model from [here](https://huggingface.co/mmwillet2/Kokoro_GGUF/tree/main).

# Build Docker Image

```sh
docker build -t smart-assistant/text-to-speech -f backbone/text-to-speech/Dockerfile .
```

```sh
make docker-text-to-speech
```
