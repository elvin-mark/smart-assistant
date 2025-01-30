cd /app

apk update && apk add git build-base make wget cmake ffmpeg

git clone https://github.com/ggerganov/llama.cpp.git && \
    cd llama.cpp && \
    mkdir build && \
    cd build &&\
    cmake .. && \
    make -j 4

cd /app

git clone https://github.com/ggerganov/whisper.cpp.git && \
    cd whisper.cpp && \
    mkdir build && \
    cd build &&\
    cmake .. && \
    make -j 4