# Speech Recognition

For the chatbot, the [OpenAI's Whisper](https://github.com/openai/whisper) model is being used, since this model it is light weigth and already good enough for this project. On top of that, to make a simple and fast inference server (without any extra dependencies), the [whisper.cpp](https://github.com/ggerganov/whisper.cpp) server and the [gguf model of Whisper](https://huggingface.co/ggerganov/whisper.cpp/tree/main) is used.

Note: Make sure to download the gguf model from [here](https://huggingface.co/ggerganov/whisper.cpp/tree/main).

# Build Docker Image
```sh
docker build -t smart-assistant/speech-recognition:1.0 .
```