FROM python:3.12-slim

WORKDIR /app

COPY ./backbone/text-to-speech/ /app/

RUN pip3 install -r requirements.txt

EXPOSE 8383

ENTRYPOINT [ "uvicorn","server:app","--host","0.0.0.0","--port","8383"]