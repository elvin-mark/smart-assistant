FROM alpine

RUN apk update && apk add git build-base make ffmpeg

RUN mkdir -p /app
RUN mkdir -p /app/models

WORKDIR /app

RUN git clone https://github.com/ggerganov/whisper.cpp.git && \
    cd whisper.cpp && \
    make 

COPY ./ggml-base.bin /app/models/

EXPOSE 8080

ENTRYPOINT [ "/app/whisper.cpp/server","-m","/app/models/ggml-base.bin" ,"--host","0.0.0.0","--port","8080","--convert"]