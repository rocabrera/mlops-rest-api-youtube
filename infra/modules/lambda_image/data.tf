data "archive_file" "src" {
  type        = "zip"
  source_dir = "${local.root_app_path}/app/src/"
  output_path = "${local.root_app_path}/app/artifacts/src_code.zip"
}