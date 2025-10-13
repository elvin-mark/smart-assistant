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

cd /app

if [ -d TTS.cpp ]; then
    cd TTS.cpp
    git pull
else
    git clone https://github.com/elvin-mark/TTS.cpp.git
    cd TTS.cpp
    git clone -b support-for-tts https://github.com/mmwillet/ggml.git
fi

apk add espeak-ng-dev sdl2-dev
# ln -s /usr/lib/libespeak-ng.so /usr/lib/libespeak-ng.o # <- no need since TTS.cpp has been updated
export ESPEAK_INSTALL_DIR=/usr
cmake -B build
cmake --build build --config Release 

cd /app