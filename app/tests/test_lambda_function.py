import json
from src.lambda_function import lambda_handler


def test_lambda_handler(lambda_context, correct_body):

    minimal_event = {
        "path": "/predict",
        "httpMethod": "POST",
        "body": json.dumps(correct_body),
        "requestContext": {"requestId": "227b78aa-779d-47d4-a48e-ce62120393b8"}
    }
    sample_size = len(correct_body)

    expected_body = json.dumps({"Classe":[0 for _ in range(sample_size)]})
    response = lambda_handler(minimal_event, lambda_context)
    expected_status = 200

    assert response["statusCode"] == expected_status
    assert response["body"] == expected_body
