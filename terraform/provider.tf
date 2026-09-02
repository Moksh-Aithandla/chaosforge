terraform {
  required_version = ">= 1.6.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project     = "ChaosForge"
      Environment = "dev"
      ManagedBy   = "Terraform"
    }
  }
}

variable "admin_ip" {
  description = "Public IP address allowed to SSH into ChaosForge EC2"
  type        = string
}

