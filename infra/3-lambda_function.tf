module "lambda_function" {
    source          = "./modules/lambda_function"
    function_name   = "lambda-ml-rest-api"
    account_id      =  data.aws_caller_identity.current.account_id
    image_id        = module.lambda_image.image_id
    bucket_arn      = module.bucket.bucket_arn
    repository_url  = module.lambda_image.repository_url
    api_gateway_arn = module.api_gateway.api_gateway_arn
    depends_on      = [module.lambda_image, module.api_gateway]
}
