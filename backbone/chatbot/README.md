# Chatbot

For the chatbot, the [Qwen3](https://huggingface.co/Qwen/Qwen3-0.6B-GGUF) model is being used, since this model it is light weigth and already good enough for this project. On top of that, to make a simple and fast inference server (without any extra dependencies), the [llama.cpp](https://github.com/ggerganov/llama.cpp) server and the [gguf model of Qwen3](https://huggingface.co/Qwen/Qwen3-0.6B-GGUF/tree/main) is used.

Note: Make sure to download the gguf model from [here](https://huggingface.co/Qwen/Qwen3-0.6B-GGUF/tree/main).

# Build Docker Image

```sh
docker build -t smart-assistant/chatbot -f backbone/chatbot/Dockerfile .
```

or

```sh
make docker-chatbot
```
