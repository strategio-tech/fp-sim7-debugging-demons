# Scribble-AI
Welcome to my project! This is a full stack application that leverages the power of GPT-3 to generate technical blogs and LinkedIn posts with ease. With this application, you can effortlessly create high-quality content for your blog or social media page, without spending hours researching and writing.

To get started, follow the instructions in the README.md file to configure your environment variables and generate build artifacts for Beanstalk. Once you have completed these steps, you'll be ready to start generating content using GPT-3.

This project is designed to be user-friendly and easy to use, even for those with little or no programming experience. Whether you're a blogger, social media manager, or just looking to create compelling content, this application is the perfect tool for you. So why wait? Let's get started and start creating amazing content today!

Scribble-AI is an AI-powered writing assistant that generates technical blog posts and "this week I learned" (TWIL) posts. This repository contains the code for the backend API as well as the front-end user interface.

### Environment Variables
Create a .env file with the following variables OR you can enter the environment variables into Beanstalk:

#### API_TOKEN
To access GPT

#### ADMIN_PASS
To create a new user

#### SALT
To generate jwt

#### For MySQL

MYSQL_HOST
MYSQL_USER
MYSQL_PASS
MYSQL_DATABASE

To setup the database and tables
`pipenv run python3 api/utils/dbSetup.py`

To launch the development server:
`python3 api/main.py`

## Launching Prod Web Server Manually

### Package for AWS Beanstalk

This will create requirements.txt and a .zip file you can upload to beanstalk.

`pipenv run build`

### Booting up EC2 on Amazon Linux

SSH into EC2 instance created by beanstalk and run command:

## Deploy Development Server

To deploy the development server:
1.  Install the Live Server extension on your code editor.
2.  Open the `Home.html` file located in the `client` folder.
3.  Click the "Go Live" button located at the bottom of the editor.
4.  This will launch a local development server and automatically open the file in your default browser.
5.  If any changes are made in the frontend code, it will automatically refresh the page in your browser and reflect the changes.

<br>

# Setting up EC2 on Amazon Linux
To set up the EC2:
`cd /var/app/current/ && chmod +x scripts/* && pipenv run start`