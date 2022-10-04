data "archive_file" "src" {
  type        = "zip"
  source_dir = "/home/rocabrera/Desktop/mlops-rest-api-youtube/app/src/"
  output_path = "/home/rocabrera/Desktop/mlops-rest-api-youtube/app/artifacts/src_code.zip"
}