FROM python:3.10.8-slim

ENV PYTHONPATH="/opt/app:${PYTHONPATH}"
ENV DJANGO_SETTINGS_MODULE='app.settings.prod'
ENV WSGI_LOG_LEVEL='error'
ENV DJANGO_LOG_LEVEL='WARNING'
ENV DATABASE_DSN='postgres://postgres:postgres@default:5432/db'
ENV RABBITMQ_DSN='amqp://guest:guest@rabbitmq//'

WORKDIR /opt/app
ADD ./app/ .

RUN apt-get -qq update && \
    apt-get -qq install --no-install-recommends --yes apache2 apache2-dev libpq-dev && \
    pip install mod_wsgi && \
    pip install -r requirements.txt && \
    apt-get -qq clean && \
    apt-get -qq autoclean && \
    apt-get -qq remove --purge --auto-remove --yes && \
    rm -rf /var/lib/apt/lists/*

CMD [ "python", "manage.py", "runmodwsgi", \
    "--port=80", \
    "--user=www-data", \
    "--group=www-data", \
    "--log-level=${WSGI_LOG_LEVEL}", \
    "--log-to-terminal" \
]
