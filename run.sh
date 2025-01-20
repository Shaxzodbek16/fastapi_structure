#!/bin/bash

pip freeze > requirements.txt

black .

uvicorn app.main.main:create_app --reload
