# Embeddings

For the embeddings, the [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) model is being used, since this model it is light weigth and already good enough for this project. On top of that, to make a simple and fast inference server (without any extra dependencies), the [llama.cpp](https://github.com/ggerganov/llama.cpp) server and the [gguf model of all-MiniLM-L6-v2](https://huggingface.co/second-state/All-MiniLM-L6-v2-Embedding-GGUF/tree/main) is used.

Note: Make sure to download the gguf model from [here](https://huggingface.co/second-state/All-MiniLM-L6-v2-Embedding-GGUF/tree/main).

# Build Docker Image

```sh
docker build -t smart-assistant/embeddings -f backbone/embeddings/Dockerfile .
```

or

```sh
make docker-embeddings
```
