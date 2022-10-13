import json
import pytest
from src.lambda_function import lambda_handler


def test_correct_lambda_handler_response(lambda_context, correct_body):

    minimal_event = {
        "path": "/predict",
        "httpMethod": "POST",
        "requestContext": {"requestId": "227b78aa-779d-47d4-a48e-ce62120393b8"},
        "body": json.dumps(correct_body)
    }

    expected_status_code = 200
    
    sample_size = len(correct_body) 
    expected_body = json.dumps({'Classe': [[0 for _ in range(sample_size)]]})
    
    response = lambda_handler(minimal_event, lambda_context)

    assert response["body"] == expected_body
    assert response["statusCode"] == expected_status_code
