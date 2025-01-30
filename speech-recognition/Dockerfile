FROM alpine

WORKDIR /app

COPY ./utils/whisper.cpp/build/src/libwhisper.* /app/lib/
COPY ./utils/whisper.cpp/build/ggml/src/*.so /app/lib/
COPY ./utils/whisper.cpp/build/bin/whisper-server /app/bin/
COPY ./speech-recognition/entrypoint.sh /app/

RUN apk add libstdc++ libgomp ffmpeg

EXPOSE 8080

ENV LD_LIBRARY_PATH=/app/lib/

ENTRYPOINT [ "sh","/app/entrypoint.sh"]