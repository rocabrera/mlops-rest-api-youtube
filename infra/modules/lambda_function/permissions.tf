resource "aws_iam_role" "lambda" {
  name                = "${var.function_name}-role"
  assume_role_policy  = data.aws_iam_policy_document.assume_policy.json
  inline_policy {
    name   = "policy-cloudwatch"
    policy = data.aws_iam_policy_document.cloudwatch.json
  }
  inline_policy {
    name   = "policy-s3"
    policy = data.aws_iam_policy_document.s3.json
  }
}

resource "aws_lambda_permission" "api_gw" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda_ml_rest_api.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${var.api_gateway_arn}/*"
}