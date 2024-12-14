FROM python:3.10-alpine

WORKDIR /app

RUN adduser --disabled-password appuser

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip && \
    rm -rf /var/cache/apk/*
    

COPY . /app/

EXPOSE ${APP_PORT}

USER appuser

ENTRYPOINT [ "./entrypoints.sh" ]

