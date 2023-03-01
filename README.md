# Scribble-AI
Welcome to my project! This is a full stack application that leverages the power of GPT-3 to generate technical blogs and LinkedIn posts with ease. With this application, you can effortlessly create high-quality content for your blog or social media page, without spending hours researching and writing.

![app](client/app.png)

To get started, follow the instructions in the README.md file to configure your environment variables and generate build artifacts for Beanstalk. Once you have completed these steps, you'll be ready to start generating content using GPT-3.

This project is designed to be user-friendly and easy to use, even for those with little or no programming experience. Whether you're a blogger, social media manager, or just looking to create compelling content, this application is the perfect tool for you. So why wait? Let's get started and start creating amazing content today!

Scribble-AI is an AI-powered writing assistant that generates technical blog posts and "this week I learned" (TWIL) posts. This repository contains the code for the backend API as well as the front-end user interface.

<br>

# Backend Setup
## Permissions for scripts

Make sure the shell scripts have the necessary permissions:
`chmod +x scripts/*`

## Environment Variables

Create a `.env` file with the following variables:
(These can be added to Beanstalk directly for production)

#### API_TOKEN
To access GPT

#### ADMIN_PASS
To create a new user

#### SALT
To generate a token

#### For MySQL

MYSQL_HOST
MYSQL_USER
MYSQL_PASS
MYSQL_DATABASE

## Database Setup

To set up the database and tables:
`pipenv run python3 api/utils/dbSetup.py`

## Start Server

To start the production server:
`pipenv run start`

To launch the development server:
`python3 api/main.py`

## Launching Prod Web Server Manually

To launch the production server manually:
`cd api/`
`gunicorn -b 0.0.0.0:80 main:app`

## Package for AWS Beanstalk

To package for AWS Beanstalk:
`pipenv run build`

## Setting up EC2 on Amazon Linux
To set up the EC2:
`cd /var/app/current/ && chmod +x scripts/* && pipenv run start`

<br>

# Frontend Setup
## Install Dependencies

To install the required dependencies:
`cd client`
`npm install`

## Deploy Development Server

To deploy the development server:
1.  Install the Live Server extension on your code editor.
2.  Open the `Home.html` file located in the `client` folder.
3.  Click the "Go Live" button located at the bottom of the editor.
4.  This will launch a local development server and automatically open the file in your default browser.
5.  If any changes are made in the frontend code, it will automatically refresh the page in your browser and reflect the changes.

<br>
