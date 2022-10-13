FROM python:3.10.7-slim

WORKDIR /opt/app
ADD ./app/ .

RUN apt-get -qq update && \
    apt-get -qq install --no-install-recommends --yes apache2 apache2-dev && \
    pip install mod_wsgi && \
    pip install -r requirements.txt && \
    apt-get -qq clean && \
    apt-get -qq autoclean && \
    apt-get -qq remove --purge --auto-remove --yes && \
    rm -rf /var/lib/apt/lists/*

ENV SERVICE_HOSTNAME=mircroservices_mr_sandwich_food_factory
ENV POSTGRES_DSN=postgres://user:password@${SERVICE_HOSTNAME}_postgres:5432/default
ENV RABBITMQ_DSN=rabbitmq://user:password@${SERVICE_HOSTNAME}_rabbitmq:15672/vhost
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LOG_LEVEL=debug

CMD [ "mod_wsgi-express", "start-server", "app/wsgi.py", \
    "--port", "80", \
    "--user", "www-data", \
    "--group", "www-data", \
    "--log-level", "$LOG_LEVEL", \
    "--log-to-terminal" \
]