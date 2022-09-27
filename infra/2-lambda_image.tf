module "lambda_image" {
    source          = "./modules/lambda_image"
    repository_name = "ecr-ml-rest-api"
    image_tag       = "latest"
    region          = var.region
    account_id      = var.account_id
}
