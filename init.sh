#!/bin/bash
nginx -s stop
cd /var/app/staging/
pipenv --python /var/app/venv/staging-LQM1lest/bin/python3
pipenv run pip install --requirement requirements.txt
cd api/ && pipenv run gunicorn -b 0.0.0.0:80 main:app