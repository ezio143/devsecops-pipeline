provider "aws" {
  region = "us-east-1"
}

# Insecure S3 bucket - no encryption, no versioning, public ACL
resource "aws_s3_bucket" "data" {
  bucket = "company-sensitive-data-bucket"
  acl    = "public-read"

  tags = {
    Environment = "production"
  }
}

# Overly permissive IAM policy - CKV_AWS_62, CKV_AWS_63
resource "aws_iam_policy" "admin" {
  name        = "overly-permissive-policy"
  description = "This policy grants full access to everything"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = "*"
        Resource = "*"
      }
    ]
  })
}


# RDS instance with no encryption and publicly accessible
resource "aws_db_instance" "database" {
  allocated_storage    = 20
  engine               = "mysql"
  engine_version       = "8.0"
  instance_class       = "db.t3.micro"
  db_name              = "appdb"
  username             = "admin"
  password             = "plaintext-password-123"
  skip_final_snapshot  = true
  publicly_accessible  = true
  storage_encrypted    = false
}