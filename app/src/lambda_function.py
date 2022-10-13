# from tester.test import dummy_function
import json
import numpy as np
from initializer import init_lambda
from http import HTTPStatus
from aws_lambda_powertools import Logger #,Tracer
# from aws_lambda_powertools.event_handler.exceptions import InternalServerError
from aws_lambda_powertools.event_handler import APIGatewayRestResolver, Response, content_types
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext
from exceptions import DownloadModelError, LoadModelError
# tracer = Tracer()

logger = Logger()
app = APIGatewayRestResolver()


estimator = init_lambda()

@app.exception_handler(DownloadModelError)
def handle_error(ex: DownloadModelError):
    logger.error(ex)
    return Response(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value,
        content_type=content_types.TEXT_PLAIN,
        body="Model could not be downloaded",
    )

@app.exception_handler(LoadModelError)
def handle_error(ex: LoadModelError):
    logger.error(ex)
    return Response(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value,
        content_type=content_types.TEXT_PLAIN,
        body="Model could not be loaded",
    )

@app.exception_handler(Exception)
def handle_error(ex: Exception):
    logger.error(ex)
    return Response(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value,
        content_type=content_types.TEXT_PLAIN,
        body="error not mapped",
    )


@app.route('/predict', method=['POST'])
# @tracer.capture_method
def predict():
    body: dict = app.current_event.json_body
    X = np.asarray([list(element.values()) for element in body])
    estimator_response: np.ndarray = estimator.predict(X)

    return Response(
            status_code=HTTPStatus.OK.value,
            content_type=content_types.APPLICATION_JSON,
            body=json.dumps({'Classe': estimator_response.tolist()}),
            headers = {}
    )


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
# @tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)

