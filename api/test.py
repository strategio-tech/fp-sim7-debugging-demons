import json
import pytest
from decouple import config
from assertpy import assert_that
import requests
from main import app

#TOKEN = config('API_TOKEN')

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client 
        


def test_handlePrompt_ok(client):
    # Prepare data for request
    data = {
        "user": "eddie",
        "topic": "TestTopic",
        "key_points": ["Data Algorithms", "Fibonacci"],
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZWRkaWUiLCJzYWx0Ijoic2RmJCVzZ29oQCU1NkZTIn0.YtNEhxGDQ3xjncO8i1btg2ExZOV6BMTwoqX5LVcJKG0" #change this for a valid token retrieve for the DB
    }
   
    headers = {"Content-Type": "application/json"}

    # Send a POST request to the server
    response = client.post('/prompt', data=json.dumps(data), headers=headers)

    # Check that the server returns a 200 OK status code
    assert_that(response.status_code).is_equal_to(requests.codes.ok)

    # Check that the server returns a JSON object containing the completion key
    response_data = json.loads(response.get_data(as_text=True))
    assert_that(response_data).contains("completion")
    
    # Check that the value of the completion key is type of string.
    assert_that(response_data["completion"]).is_instance_of(str)

def test_handlePrompt_invalid_token(client):
    # Prepare data for request
    data = {
        "user": "eddie",
        "topic": "TestTopic",
        "key_points": ["Data Algorithms", "Fibonacci"],
        "token": "yJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZWRkaWUiLCJzYWx0Ijoic2RmJCVzZ29oQCU1NkZTIn0.YtNEhxGDQ3xjncO8i1btg2ExZOV6BMTwoqX5LVcJKG0"
    }
   
    headers = {"Content-Type": "application/json"}

    # Send a POST request to the server
    response = client.post('/prompt', data=json.dumps(data), headers=headers) #Not sure if headers if necessary I think no

    # Check that the server returns a 401 status code
    assert_that(response.status_code).is_equal_to(requests.codes.unauthorized)

    # Check that the server returns a message for the invalid token error
    response_data = json.loads(response.get_data(as_text=True))
    assert_that(response_data['message']).is_equal_to("Invalid token.")
    
   
    

   
    







