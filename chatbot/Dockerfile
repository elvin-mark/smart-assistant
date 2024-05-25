FROM alpine

RUN apk update && apk add git build-base make

RUN mkdir -p /app
RUN mkdir -p /app/models

WORKDIR /app

RUN git clone https://github.com/ggerganov/llama.cpp.git && \
    cd llama.cpp && \
    make 

COPY ./tinyllama-1.1b-chat-v1.0.Q8_0.gguf /app/models/

EXPOSE 8181

ENTRYPOINT [ "/app/llama.cpp/server","-m","/app/models/tinyllama-1.1b-chat-v1.0.Q8_0.gguf" ,"--host","0.0.0.0","--port","8181"]