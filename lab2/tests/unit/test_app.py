import json
from training_api import ComputeFactorialRequest, ComputeFactorialResponse

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