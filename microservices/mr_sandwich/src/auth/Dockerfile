FROM alpine:3.15.6

ADD . /opt
WORKDIR /opt

RUN apk add --update --no-cache python3 \
    && ln -sf python3 /usr/bin/python \
    && python3 -m ensurepip \
    && python -m venv venv \
    && pip3 install -r requirements.txt --quiet

ENTRYPOINT /opt/entrypoint.sh