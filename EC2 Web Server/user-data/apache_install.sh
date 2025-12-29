#!/bin/bash
# EC2 User Data Script: Install Apache & Deploy Web Page

yum update -y
yum install httpd -y

systemctl start httpd
systemctl enable httpd

echo "<h1>Hello World from EC2</h1>" > /var/www/html/index.html