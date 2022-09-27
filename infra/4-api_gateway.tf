module "api_gateway" {
    source          = "./modules/api_gateway"
    region          = var.region
    account_id      = var.account_id
    function_name   = "lambda-ml-rest-api"
}
