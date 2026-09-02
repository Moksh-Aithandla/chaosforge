resource "aws_instance" "chaosforge" {
  ami           = "ami-050c78efa486a0196"
  instance_type = "t3.micro"

  key_name = "chaosforge-key"

  subnet_id              = aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.ec2.id]

  iam_instance_profile = aws_iam_instance_profile.ec2.name

  associate_public_ip_address = true

  root_block_device {
    volume_size = 8
    volume_type = "gp3"
  }

  tags = {
    Name = "${var.project_name}-ec2"
  }

}