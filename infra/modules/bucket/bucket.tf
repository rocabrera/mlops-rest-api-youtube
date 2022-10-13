resource "aws_s3_bucket" "bucket" {
  bucket = "${var.account_id}-${var.bucket_name}"
}

resource "aws_s3_bucket_acl" "acl" {
  bucket = aws_s3_bucket.bucket.id
  acl    = "private"
}

resource "aws_s3_object" "object" {
  key                    = "model.pickle"
  bucket                 = aws_s3_bucket.bucket.id
  source                 = "/home/rocabrera/Desktop/mlops-rest-api-youtube/app/artifacts/model.pickle"
}