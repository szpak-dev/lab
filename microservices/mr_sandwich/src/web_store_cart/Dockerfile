FROM python:3.10.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV WSGI_LOG_LEVEL=warning
ENV APP_LOG_LEVEL=warning
ENV DATABASE_DSN=postgres://postgres:postgres@default:5432/db
ENV RABBITMQ_DSN=amqp://guest:guest@rabbitmq//

WORKDIR /opt/app
ADD ./app/ .

RUN pip install -r requirements.txt --quiet --no-cache-dir

CMD [ "python", "main.py" ]