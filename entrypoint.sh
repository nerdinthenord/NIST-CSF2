#!/bin/sh
set -e

python seed_db.py

exec uvicorn app:app --host 0.0.0.0 --port 8000
