FROM python:3.10.8-slim as base

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV WSGI_LOG_LEVEL=warning
ENV APP_LOG_LEVEL=warning
ENV DATABASE_DSN=postgresql://postgres:postgres@default:5432/db
ENV RABBITMQ_DSN=amqp://guest:guest@rabbitmq//

FROM base AS deps
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

FROM base AS runtime
WORKDIR /opt/app
COPY --from=deps /.venv .venv
ENV PATH="/opt/app/.venv/bin:$PATH"
ADD . .

CMD [ "python", "main.py" ]