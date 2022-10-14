import json
from http import HTTPStatus
import numpy as np
from aws_lambda_powertools import Logger #, Tracer
from aws_lambda_powertools.event_handler.exceptions import InternalServerError 
from aws_lambda_powertools.event_handler import APIGatewayRestResolver, Response, content_types
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext
from initializer import init_lambda

# tracer = Tracer()
logger = Logger()
app = APIGatewayRestResolver()

estimator = init_lambda()

@app.exception_handler(Exception)
def handle_invalid_limit_qs(ex: Exception): 
    logger.exception("Um erro aconteceu")
    raise InternalServerError("An error occurred.")

@app.route('/predict', method=['POST'])
# @tracer.capture_method
def predict():
    logger.info("Entrei na rota") 

    body: dict = app.current_event.json_body

    X = np.asarray([list(element.values()) for element in body])

    estimator_response: np.ndarray = estimator.predict(X)
    return Response(
        status_code=HTTPStatus.OK.value,
        content_type=content_types.APPLICATION_JSON,
        body=json.dumps({"Classe": estimator_response.tolist()}),
        headers={}
    )

# You can continue to use other utilities just as before
@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
# @tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)
