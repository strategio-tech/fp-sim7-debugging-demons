#!/bin/bash
nginx -s stop
cd /var/app/current/
pipenv run pip install --requirement requirements.txt
cd api/ && pipenv run gunicorn -b 0.0.0.0:80 main:app