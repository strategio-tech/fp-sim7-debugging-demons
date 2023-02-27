# Scribble-AI



## Initial Setup

### Environment Variables
Create a .env file with the following variables:

#### API_TOKEN
To access GPT

#### ADMIN_PASS
To create a new user

#### SALT
To generate a token

#### For MYSQL
##### MYSQL_HOST
##### MYSQL_USER
##### MYSQL_PASS
##### MYSQL_DATABASE

### Before Running API

Run commands from root directory:

First launch virtual env
pipenv shell

To install dependencies
pipenv install

To setup the database and tables
python3 api/utils/dbSetup.py

### Launching Web Server

cd api

Localy for testing: gunicorn -b 127.0.0.1:3030 main:app
For production: gunicorn -b 0.0.0.0:80 main:app

### Launch Dev Server

From root directory run

python3 api/main.py

### Package for AWS Beanstalk

python3 -m pipenv run pip freeze > requirements.txt && python3 -m pipenv run pip install --requirement requirements.txt && zip -r scribble-ai.zip . -x "*.git*" "*.venv*" "*.vscode*" "*.idea*" "*.DS_Store*"

### Setting up EC2 on Amazon Linux

cd /var/app/staging/
chmod +x init.sh
./init.sh
