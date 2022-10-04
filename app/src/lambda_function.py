# from tester.test import dummy_function
import json
import numpy as np
from http import HTTPStatus
from aws_lambda_powertools import Logger #,Tracer
from aws_lambda_powertools.event_handler.exceptions import InternalServerError
from aws_lambda_powertools.event_handler import APIGatewayRestResolver, Response, content_types
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext

# tracer = Tracer()

logger = Logger()
app = APIGatewayRestResolver()

@app.exception_handler(Exception)
def handle_error(ex: Exception):
    raise InternalServerError("An error occurred")


@app.route('/predict', method=['POST'])
# @tracer.capture_method
def predict():

    body: dict = app.current_event.json_body

    X = np.array(list(body.values())).reshape(1,-1)

    logger.info(X)

    return Response(
            status_code=HTTPStatus.OK.value,
            content_type=content_types.APPLICATION_JSON,
            body = json.dumps({"status": "success", "data": "Teste"}),
            headers = {"Content-Type": "application/json"}
    )

@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
# @tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)

