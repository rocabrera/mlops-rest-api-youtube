data "archive_file" "src" {
  type        = "zip"
  source_dir = "/home/rocabrera/Desktop/mlops-learning/projects/ml_rest_api/app/src/"
  output_path = "modules/lambda_image/src_code.zip"
}