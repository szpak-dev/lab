FROM alpine:3.15.6

ADD . /opt
WORKDIR /opt

ENV PATH="${PATH}:/opt/sh"

RUN apk add --update --no-cache python3 libpq postgresql-client \
    && ln -sf python3 /usr/bin/python \
    && python3 -m ensurepip \
    && pip3 install --no-cache --upgrade pip setuptools

ENTRYPOINT /opt/entrypoint.sh
