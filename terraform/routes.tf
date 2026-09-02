resource "aws_internet_gateway" "chaosforge" {
  vpc_id = aws_vpc.chaosforge.id

  tags = {
    Name = "${var.project_name}-igw"
  }
}
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.chaosforge.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.chaosforge.id
  }

  tags = {
    Name = "${var.project_name}-public-rt"
  }
}
resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}
resource "aws_route_table" "private" {
  vpc_id = aws_vpc.chaosforge.id

  tags = {
    Name = "${var.project_name}-private-rt"
  }
}
resource "aws_route_table_association" "private" {
  subnet_id      = aws_subnet.private.id
  route_table_id = aws_route_table.private.id
}