from flask import Flask, request, jsonify
from decouple import config
import requests

from utils.util import authenticate_password, hash_password

TOKEN = config('API_TOKEN')

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def signup():
    # Get the data from the POST request
    data = request.get_json()

    # Process the data
    hash = hash_password(data['password'])

    # write code to store in db

    # Return a response
    response = {"message": data}
    return jsonify(response)

@app.route('/login', methods=['POST'])
def login():
    # Get the data from the POST request
    hash = request.get_json()

    #write code to request password from db
    password = ''

    # Process the data
    isValid = authenticate_password(data['password'], hash)

    # if valid retrieve search history

    # Return a response
    response = {"authenticated": isValid}
    return jsonify(response)

# Route to handle POST requests to /api/second_route
@app.route('/prompt', methods=['POST'])
def handlePrompt():
    # Get the data from the POST request
    data = request.get_json()

    # Process the data
    # ...

    # Return a response
    response = {"completion": data}
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=3030,debug=True)