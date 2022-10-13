FROM python:3.9.14-alpine3.16

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POSTGRES_DSN=postgres://user:password@mircroservices_mr_sandwich_food_factory_postgres:5432/default
ENV RABBITMQ_DSN=rabbitmq://user:password@mircroservices_mr_sandwich_food_factory_rabbitmq:15672/vhost

ADD ./app /opt/app
WORKDIR /opt/app

RUN apk add --no-cache uwsgi-python3 && \
    pip3 install --upgrade pip --quiet && \
    pip3 install -r requirements.txt --quiet

CMD ["uwsgi", "django.ini"]
