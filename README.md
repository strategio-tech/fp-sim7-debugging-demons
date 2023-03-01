# Scribble-AI

## Initial Setup

### Permissions for scripts
chmod +x build.sh prod.sh init.sh

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

To setup the database and tables
pipenv shell
python3 api/utils/dbSetup.py

### To start production server 

pipenv run start

### Launch Dev Server

From root directory run

python3 api/main.py

### Launching Prod Web Server Manually

cd api/

Locally for testing: gunicorn -b 127.0.0.1:3030 main:app
For production: gunicorn -b 0.0.0.0:80 main:app

### Package for AWS Beanstalk

pipenv run build

### Front End Setup

npm install

### Deploy Front End Development Server with Live Server

Install Live Server extension
Open the Home.html file located in the client folder
Click the "Go Live" button located at the bottom of the editor
This will launch a local development server and automatically open the file in your default browser
If any changes are made in the front end code, it will automatically refresh the page in your browser and reflect the changes

### Setting up EC2 on Amazon Linux

cd /var/app/current/ && chmod +x scripts/* && pipenv run start