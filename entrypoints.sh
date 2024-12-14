#!/bin/sh
alembic upgrade head
rm -rf /app/migrations/__pycache__
python main.py
