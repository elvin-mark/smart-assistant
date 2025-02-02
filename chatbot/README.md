# Chatbot

For the chatbot, the [TinySwallow](https://huggingface.co/SakanaAI/TinySwallow-1.5B-Instruct) model is being used, since this model it is light weigth and already good enough for this project. On top of that, to make a simple and fast inference server (without any extra dependencies), the [llama.cpp](https://github.com/ggerganov/llama.cpp) server and the [gguf model of TinySwallow](https://huggingface.co/SakanaAI/TinySwallow-1.5B-Instruct-GGUF) is used.

Note: Make sure to download the gguf model from [here](https://huggingface.co/SakanaAI/TinySwallow-1.5B-Instruct-GGUF/tree/main).

# Build Docker Image

```sh
docker build -t smart-assistant/chatbot -f chatbot/Dockerfile .
```

or 

```sh
make docker-chatbot
```