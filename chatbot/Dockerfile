FROM alpine

WORKDIR /app

COPY ./utils/llama.cpp/build/bin/*.so /app/lib/
COPY ./utils/llama.cpp/build/bin/llama-server /app/bin/
COPY ./chatbot/entrypoint.sh /app/
RUN apk add libstdc++ libgomp

EXPOSE 8181

ENV LD_LIBRARY_PATH=/app/lib/

ENTRYPOINT [ "sh","/app/entrypoint.sh"]