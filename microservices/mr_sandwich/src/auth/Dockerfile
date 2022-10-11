FROM python:3.9.14-alpine3.16

ADD . /opt
WORKDIR /opt

RUN pip3 install --upgrade pip --quiet && pip3 install -r requirements.txt --quiet

ENTRYPOINT /opt/entrypoint.sh