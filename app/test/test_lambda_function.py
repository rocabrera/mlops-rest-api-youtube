import json
from src.lambda_function import lambda_handler


def test_lambda_handler(lambda_context):
    minimal_event = {
        "path": "/predict",
        "httpMethod": "POST",
        "requestContext": {"requestId": "227b78aa-779d-47d4-a48e-ce62120393b8"},
        "body": json.dumps({"test1":1, "test2":2})
    }

    expected_status_code = 200
    # expected_body = json.dumps({"Param":"Funciona"})
    
    response = lambda_handler(minimal_event, lambda_context)
    assert response["statusCode"] == expected_status_code
    # assert response["body"] == expected_body
