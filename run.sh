#!/bin/bash

pip freeze > requirements.txt

black .

python feed.py

uvicorn app.server.main:create_app --host 0.0.0.0 --port 8000 --reload --factory
