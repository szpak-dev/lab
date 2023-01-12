FROM python:3.10.8-slim as builder

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir --upgrade pipenv
RUN PIPENV_VENV_IN_PROJECT=1 pipenv sync

FROM python:3.10.8-slim

ENV WSGI_LOG_LEVEL=warning
ENV APP_LOG_LEVEL=warning
ENV DATABASE_DSN=postgresql://postgres:postgres@default:5432/db
ENV RABBITMQ_DSN=amqp://guest:guest@rabbitmq//
ENV JWT_SECRET=jwt_secret

WORKDIR /app
COPY --from=builder /app .
ENV PATH="/app/.venv/bin:$PATH"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
