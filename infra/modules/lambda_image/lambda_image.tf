resource null_resource ecr_image {
 triggers = {
   python_code = data.archive_file.src.output_sha
   docker_file = md5(file("/home/rocabrera/Desktop/mlops-learning/projects/ml_rest_api/app/Dockerfile"))
 }
 provisioner "local-exec" {
   command = <<EOF
           aws ecr get-login-password --region ${var.region} | docker login --username AWS --password-stdin ${var.account_id}.dkr.ecr.${var.region}.amazonaws.com
           cd /home/rocabrera/Desktop/mlops-learning/projects/ml_rest_api/app
           docker build -t ${aws_ecr_repository.repo.repository_url}:${var.image_tag} .
           docker push ${aws_ecr_repository.repo.repository_url}:${var.image_tag}
       EOF
 }
}

resource aws_ecr_repository repo {
 name = var.repository_name
 force_delete = true
}
 
data aws_ecr_image lambda_image {
 depends_on = [
   null_resource.ecr_image
 ]
 repository_name = var.repository_name
 image_tag       = var.image_tag
}