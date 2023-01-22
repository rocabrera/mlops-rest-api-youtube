data "aws_caller_identity" "current" {}

resource "aws_lambda_function" "lambda_ml_rest_api" {
  function_name = var.function_name
  role          = aws_iam_role.lambda.arn
  image_uri     = "${var.repository_url}@${var.image_id}"
  package_type  = "Image"

  environment {
    variables = {
      ACCOUNT_ID = data.aws_caller_identity.current.account_id
    }
  }
}