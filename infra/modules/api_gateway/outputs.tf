output api_gateway_arn {
    value = aws_api_gateway_rest_api.rest_gateway.execution_arn
}

output predict_route {
    value = "https://${aws_api_gateway_rest_api.rest_gateway.id}.execute-api.${var.region}.amazonaws.com/${local.stage_name}/${local.route_name}"
}