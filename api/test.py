import json
import pytest
from decouple import config
from assertpy import assert_that
import requests
from main import app

#TOKEN = config('API_TOKEN')
ADMIN_PASSWORD = config('ADMIN_PASS')
headers = {"Content-Type": "application/json"}

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
    
   
    # assert response.json["name"] == "testuser"
    # assert response.json["token"] is not None
    # assert len(response.json["promptHistory"]) >= 0 


def test_signup_new_user(client):
    # Prepare data for the request
    data = {
        "name": "Test User",
        "user": "testUser",
        "password": "mysecretpassword",
        "admin_password": ADMIN_PASSWORD
    }
   
    # Make a POST request to the signup endpoint
    response = client.post('/signup', data=json.dumps(data), headers=headers)

    # Check that the response status code is 200
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    
    # Check that the response contains the correct user data
    response_data = json.loads(response.get_data(as_text=True))
    assert_that(response_data["name"]) == "testuser"
    assert_that(response_data["token"]).is_not_none
    assert_that(len(response_data["promptHistory"])).is_greater_than(0)
   
      
def test_signup_existing_user(client):

    # Prepare duplicate data for another request with the same username
    data_duplicate = {
        "name": "Other Test User",
        "user": "testUser",
        "password": "mysecretpassword",
        "admin_password": ADMIN_PASSWORD
    }
  
    # Make another POST request to the signup endpoint with the same username
    response_duplicate = client.post('/signup', data=json.dumps(data_duplicate), headers=headers)
   
    # Check that the response status code is 400 because the user already 
    assert_that(response_duplicate.status_code).is_equal_to(requests.codes.bad_request)
    
    # Check that the response has the correct message
    response_duplicate_data = json.loads(response_duplicate.get_data(as_text=True))
    assert_that(response_duplicate_data["message"]).is_equal_to("This user already exists.")
  

def test_signup_invalid_admin_password(client):
    # Prepare data for a request with an invalid admin password
    data = {
        "name": "Other Test User2",
        "user": "testUser2",
        "password": "mysecretpassword",
        "admin_password": "wrong password"
    }   
    
    # Make a POST request to the signup endpoint with the wrong password
    response= client.post('/signup', data=json.dumps(data), headers=headers)

    # Check that the response status code is 401 because the password is incorrect
    assert_that(response.status_code).is_equal_to(requests.codes.unauthorized)
    
   # Check that the response data has the correct message
    response_data = json.loads(response.get_data(as_text=True))
    assert_that(response_data["message"]).is_equal_to("Invalid admin password")
    

   
    







