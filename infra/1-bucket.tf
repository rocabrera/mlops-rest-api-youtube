module "bucket" {
    source = "./modules/bucket"
    account_id = data.aws_caller_identity.current.account_id
    bucket_name = "ml-rest-api"
}