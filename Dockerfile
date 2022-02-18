FROM alpine:3.14

RUN mkdir /src

WORKDIR /src

RUN apk update && apk add python3 && apk add unzip

COPY script.py .

CMD python3 script.py
