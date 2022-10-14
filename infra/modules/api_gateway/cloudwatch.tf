resource aws_cloudwatch_log_group "cloudwatch" {
    name = "API-Gateway-Execution-Logs_${aws_api_gateway_rest_api.rest_gateway.id}/${local.stage_name}"
    retention_in_days = 1
}

resource aws_api_gateway_account "gateway_account" {
    cloudwatch_role_arn = aws_iam_role.cloudwatch.arn
}

resource "aws_iam_role" "cloudwatch" {
  name               = "api_gateway_cloudwatch"
  assume_role_policy = data.aws_iam_policy_document.gateway-assume-role-policy.json

  inline_policy {
    name   = "policy-cloudwatch"
    policy = data.aws_iam_policy_document.inline_cloudwatch_policy.json
  }
}

data "aws_iam_policy_document" "inline_cloudwatch_policy" {
  statement {
    actions   = [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:DescribeLogGroups",
        "logs:DescribeLogStreams",
        "logs:PutLogEvents",
        "logs:GetLogEvents",
        "logs:FilterLogEvents",
    ]
    resources = ["*"]
  }
}

data "aws_iam_policy_document" "gateway-assume-role-policy" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["apigateway.amazonaws.com"]
    }
  }
}
