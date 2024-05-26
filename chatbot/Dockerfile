FROM alpine

RUN apk update && apk add git build-base make wget

RUN mkdir -p /app
RUN mkdir -p /app/models

WORKDIR /app

RUN git clone https://github.com/ggerganov/llama.cpp.git && \
    cd llama.cpp && \
    make 

# COPY ./tinyllama-1.1b-chat-v1.0.Q8_0.gguf /app/models/
RUN wget -O /app/models/tinyllama-1.1b-chat-v1.0.Q8_0.gguf https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q8_0.gguf?download=true

EXPOSE 8181

ENTRYPOINT [ "/app/llama.cpp/server","-m","/app/models/tinyllama-1.1b-chat-v1.0.Q8_0.gguf" ,"--host","0.0.0.0","--port","8181"]