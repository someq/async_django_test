#!/usr/bin/env bash

source venv/bin/activate
gunicorn --bind 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker --reload async_example.asgi:application
