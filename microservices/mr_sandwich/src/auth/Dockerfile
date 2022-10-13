FROM python:3.10.7-slim

WORKDIR /opt/app
ADD ./app/ .

RUN apt-get update && \
    apt-get install --no-install-recommends --yes apache2 apache2-dev && \
    pip install mod_wsgi && \
    pip install -r requirements.txt && \
    apt-get remove --yes python-pip && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

ENV SERVICE_HOSTNAME=mircroservices_mr_sandwich_auth
ENV POSTGRES_DSN=postgres://user:password@${SERVICE_HOSTNAME}_postgres:5432/default
ENV RABBITMQ_DSN=rabbitmq://user:password@${SERVICE_HOSTNAME}_rabbitmq:15672/vhost
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LOG_LEVEL=debug

CMD [ "mod_wsgi-express", "start-server", "wsgi.py", \
    "--port", "80", \
    "--user", "www-data", \
    "--group", "www-data", \
    "--log-level", "$LOG_LEVEL", \
    "--log-to-terminal" \
]