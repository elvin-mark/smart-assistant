# Text-to-Speech

For the chatbot, the [KokoroTTS](https://github.com/hexgrad/kokoro) model is being used, since this model it is light weigth and already good enough for this project. On top of that, to make a simple and fast inference server, the [onnxruntime inference engine](https://github.com/microsoft/onnxruntime) server and the [onnx model of KokoroTTS](https://huggingface.co/onnx-community/Kokoro-82M-v1.0-ONNX/tree/main/onnx) is used.

Note: Make sure to download the onnx model from [here](https://huggingface.co/onnx-community/Kokoro-82M-v1.0-ONNX/tree/main/onnx).

# Build Docker Image

```sh
docker build -t smart-assistant/text-to-speech -f text-to-speech/Dockerfile .
```

```sh
make docker-text-to-speech
```
