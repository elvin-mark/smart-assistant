# Chatbot

For the chatbot, the [Gemma3](https://huggingface.co/unsloth/gemma-3-270m-it-GGUF) model is being used, since this model it is light weigth and already good enough for this project. On top of that, to make a simple and fast inference server (without any extra dependencies), the [llama.cpp](https://github.com/ggerganov/llama.cpp) server and the [gguf model of Gemma3](https://huggingface.co/unsloth/gemma-3-270m-it-GGUF/tree/main) is used.

Note: Make sure to download the gguf model from [here](https://huggingface.co/unsloth/gemma-3-270m-it-GGUF/tree/main).

# Build Docker Image

```sh
docker build -t smart-assistant/chatbot -f backbone/chatbot/Dockerfile .
```

or

```sh
make docker-chatbot
```
