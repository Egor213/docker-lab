FROM python:3.10-alpine

WORKDIR /app

RUN adduser -D appuser

COPY requirements.txt /app/

RUN rm -rf /root/.cache/pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

ENV USER=${USER}
ENV PASSWORD=${PASSWORD}
ENV SERVER=${SERVER}
ENV DATABASE=${DATABASE}
ENV PORT=${PORT}
ENV APP_HOST=${APP_HOST}
ENV APP_PORT=${APP_PORT}

EXPOSE ${APP_PORT}

USER appuser

CMD echo "USER=${USER}" > .env && \
    echo "PASSWORD=${PASSWORD}" >> .env && \
    echo "SERVER=${SERVER}" >> .env && \
    echo "DATABASE=${DATABASE}" >> .env && \
    echo "PORT=${PORT}" >> .env && \
    echo "APP_HOST=${APP_HOST}" >> .env && \
    echo "APP_PORT=${APP_PORT}" >> .env && \
    alembic upgrade head && \
    python main.py
