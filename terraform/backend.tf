terraform {
  backend "s3" {
    bucket = "your-bucket-aws"
    key    = "core/terraform.tfstate"
    region = "us-east-1"
  }
}