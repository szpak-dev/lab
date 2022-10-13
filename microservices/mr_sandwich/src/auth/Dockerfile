FROM python:3.10.7-slim

WORKDIR /opt/app
ADD ./app/ .

RUN pip3 install uwsgi && \
    pip3 install -r requirements.txt

ENV SERVICE_HOSTNAME=mircroservices_mr_sandwich_food_factory
ENV POSTGRES_DSN=postgres://user:password@${SERVICE_HOSTNAME}_postgres:5432/default
ENV RABBITMQ_DSN=rabbitmq://user:password@${SERVICE_HOSTNAME}_rabbitmq:15672/vhost
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

