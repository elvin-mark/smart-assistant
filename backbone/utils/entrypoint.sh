cd /app

apk update && apk add git build-base make wget cmake ffmpeg linux-headers curl-dev

if [ -d llama.cpp ]; then
    cd llama.cpp
    git pull
else
    git clone https://github.com/ggerganov/llama.cpp.git
    cd llama.cpp
fi

mkdir -p build && \
    cd build &&\
    cmake .. && \
    make -j4

cd /app

if [ -d whisper.cpp ]; then
    cd whisper.cpp
    git pull
else
    git clone https://github.com/ggerganov/whisper.cpp.git
    cd whisper.cpp
fi

mkdir -p build && \
    cd build &&\
    cmake .. && \
    make -j4