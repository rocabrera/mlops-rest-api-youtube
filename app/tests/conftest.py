import pytest
from dataclasses import dataclass
import sys
import json

import numpy as np

class FakeEstimator:

    def predict(self, X: np.ndarray):
        rows, _ = X.shape
        return np.asarray([0 for _ in range(rows)])

class FakeInit:

    @staticmethod
    def init_lambda():
        return FakeEstimator()

sys.modules["initializer"] = FakeInit()

@pytest.fixture(scope="module")
def lambda_context():
    @dataclass
    class LambdaContext:
        function_name: str = "test"
        memory_limit_in_mb: int = 128
        invoked_function_arn: str = "arn:aws:lambda:eu-west-1:123456789012:function:test"
        aws_request_id: str = "da658bd3-2d6f-4e7b-8ec2-937234644fdc"

    return LambdaContext()

@pytest.fixture(scope="module",params=[
    "body_single_entrie", "body_multiple_entries"
])
def correct_body(request) -> dict:
    with open(f"tests/data/{request.param}.json", "rb") as f:
        data = json.load(f)

    return data