#!/bin/bash
nginx -s stop
cd /var/app/current/
pip install --requirement requirements.txt
cat /opt/elasticbeanstalk/deployment/env > .env
cd api/ && gunicorn -b 0.0.0.0:80 main:app