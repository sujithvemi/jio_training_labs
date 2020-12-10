import json
from app.lab.models.models import ComputeFactorialRequest, ComputeFactorialResponse
from app.lab.models.models import CheckPrimeRequest, CheckPrimeResponse
from app.lab.models.models import RemoveDuplicateRequest, RemoveDuplicateResponse

def test_factorial_server(test_client):
    request = ComputeFactorialRequest(n=5)
    # request['n'] = 5
    query = {}
    body = json.loads(request.json())
    headers = {
        "Content-Type" : "application/json"
    }

    url = "/compute/factorial/"

    response = test_client.post(url, json=body, params=query, headers=headers)
    assert response.status_code == 200
    result_dict = response.json()
    result = ComputeFactorialResponse(**result_dict)
    assert result.input_n == 5
    assert result.factorial_val == 120
    assert result.time_taken is not None

def test_prime_server(test_client):
    request = CheckPrimeRequest(n=13)
    # request['n'] = 5
    query = {}
    body = json.loads(request.json())
    headers = {
        "Content-Type" : "application/json"
    }

    url = "/compute/checkPrime/"

    response = test_client.post(url, json=body, params=query, headers=headers)
    assert response.status_code == 200
    result_dict = response.json()
    result = CheckPrimeResponse(**result_dict)
    assert result.input_n == 13
    assert result.is_prime == "true"
    assert result.time_taken is not None

def test_remove_dups_server(test_client):
    request = RemoveDuplicateRequest(text="hello how are you")
    # request['n'] = 5
    query = {}
    body = json.loads(request.json())
    headers = {
        "Content-Type" : "application/json"
    }

    url = "/text/removeDuplicate"

    response = test_client.post(url, json=body, params=query, headers=headers)
    assert response.status_code == 200
    result_dict = response.json()
    result = RemoveDuplicateResponse(**result_dict)
    assert result.input_text == "hello how are you"
    assert result.result == "helo w ar yu"
    assert result.time_taken is not None
