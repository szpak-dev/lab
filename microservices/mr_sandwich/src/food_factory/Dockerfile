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

ENV POSTGRES_DSN=postgres://user:password@${SERVICE_HOSTNAME}_postgres:5432/default
ENV RABBITMQ_DSN=amqp://guest:guest@microservices_mr_sandwich_rabbitmq//
ENV LOG_LEVEL=debug

#CMD ["python", "manage.py", "runmodwsgi"]
CMD [ "python", "manage.py", "runmodwsgi", \
    "--port=80", \
    "--user=www-data", \
    "--group=www-data", \
    "--log-level=${LOG_LEVEL}", \
    "--log-to-terminal" \
]