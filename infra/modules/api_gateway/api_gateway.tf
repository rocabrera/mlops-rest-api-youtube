resource "aws_api_gateway_rest_api" "rest_gateway" {
  body = jsonencode({
    openapi = "3.0.1"
    info = {
      title   = "example"
      version = "1.0"
    }
    paths = {
      "/predict" = {
        get = {
          x-amazon-apigateway-integration = {
            httpMethod           = "POST"
            payloadFormatVersion = "1.0"
            type                 = "AWS_PROXY"
            uri                  = "arn:aws:apigateway:${var.region}:lambda:path/2015-03-31/functions/arn:aws:lambda:${var.region}:${var.account_id}:function:${var.function_name}/invocations"
          }
        }
      }
    }
  })

  name = "rest_gateway"

  endpoint_configuration {
    types = ["REGIONAL"]
  }
}

resource "aws_api_gateway_deployment" "rest_gateway" {
  rest_api_id = aws_api_gateway_rest_api.rest_gateway.id

  triggers = {
    redeployment = sha1(jsonencode(aws_api_gateway_rest_api.rest_gateway.body))
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_api_gateway_stage" "rest_gateway" {
  deployment_id = aws_api_gateway_deployment.rest_gateway.id
  rest_api_id   = aws_api_gateway_rest_api.rest_gateway.id
  stage_name    = "rest_gateway"
}