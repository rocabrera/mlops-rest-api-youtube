module "bucket" {
    source = "./modules/bucket"
    account_id = var.account_id
    bucket_name = "ml-rest-api"
}