FROM alpine

WORKDIR /app

COPY ./backbone/utils/llama.cpp/build/bin/*.so /app/lib/
COPY ./backbone/utils/llama.cpp/build/bin/llama-server /app/bin/
COPY ./backbone/chatbot/entrypoint.sh /app/
RUN apk add libstdc++ libgomp

EXPOSE 8181

ENV LD_LIBRARY_PATH=/app/lib/

ENTRYPOINT [ "sh","/app/entrypoint.sh"]