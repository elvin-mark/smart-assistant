# Chatbot

For the chatbot, the [Tiny LLama](https://github.com/jzhang38/TinyLlama) model is being used, since this model it is light weigth and already good enough for this project. On top of that, to make a simple and fast inference server (without any extra dependencies), the [llama.cpp](https://github.com/ggerganov/llama.cpp) server and the [gguf model of Tiny Llama](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/tree/main) is used.

Note: Make sure to download the gguf model from [here](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/tree/main).

# Build Docker Image

```sh
docker build -t smart-assistant/chatbot:1.0 .
```