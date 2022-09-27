output "image_id" {
  value = data.aws_ecr_image.lambda_image.id
}

output "repository_url" {
  value = aws_ecr_repository.repo.repository_url
}
