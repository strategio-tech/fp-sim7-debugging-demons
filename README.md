# Initial Setup

## Environment Variables
Create a .env file with the following variables:

### API_TOKEN
To access GPT

### ADMIN_PASS
To create a new user

### SALT
To generate a token

### For MYSQL
#### MYSQL_HOST
#### MYSQL_USER
#### MYSQL_PASS
#### MYSQL_DATABASE

## Before Running API
Run commands from root directory:

To install dependencies
$ python3 -m pipenv install

To setup the database and tables
$ python3 api/utils/dbSetup.py
