import json
import pytest
from assertpy import assert_that
import requests
import main



# TOKEN = config('API_TOKEN')

@pytest.fixture
def client():
    main.app.config['TESTING'] = True
    with main.app.test_client() as client:
        yield client 
        


def test_handlePrompt(client):
    # Prepare data for request
    data = {
        "user": "TestUser",
        "topic": "TestTopic",
        "key_points": ["Data Algorithms", "Fibonacci"],
        "token": "valid_token"
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
   
    







