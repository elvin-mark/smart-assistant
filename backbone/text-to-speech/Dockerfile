FROM alpine

WORKDIR /app

COPY ./backbone/utils/TTS.cpp/build/bin/tts-server /app/bin/
COPY ./backbone/text-to-speech/entrypoint.sh /app/

RUN apk add libstdc++ libgomp espeak-ng-dev

EXPOSE 8383

ENTRYPOINT [ "sh","/app/entrypoint.sh"]