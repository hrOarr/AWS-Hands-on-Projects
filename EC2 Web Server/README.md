# AWS EC2 User Data – Web Server Deployment

This project demonstrates how to launch an AWS EC2 free-tier instance and automatically install and configure a web server using **EC2 User Data**.

It is designed as a hands-on lab for **AWS Solutions Architect – Associate** preparation and DevOps fundamentals.

---

## 🧪 What This Project Does

- Launches a free-tier eligible EC2 instance (t2.micro)
- Uses EC2 User Data to:
  - Update the OS
  - Install Apache HTTP Server
  - Start and enable the service
  - Deploy a simple "Hello World" web page
- Allows HTTP/HTTPS access via Security Groups

---

## 🛠️ Technologies Used

- AWS EC2
- Amazon Linux 2 / Amazon Linux 2023
- Apache HTTP Server
- Bash scripting
- EC2 User Data (cloud-init)
- AWS Security Group

---

## 🚀 How to Use

### 1️⃣ Launch EC2 Instance

- AMI: Amazon Linux 2 / Amazon Linux 2023
- Instance Type: t2.micro (Free Tier)
- Key Pair: Create or select one
- Security Group:
  - SSH (22) → Your IP
  - HTTP (80) → Anywhere
  - HTTPS (443) → Anywhere

---

### 2️⃣ Add User Data Script

Paste the following script in **Advanced details → User data**:

```bash
#!/bin/bash
yum update -y
yum install httpd -y
systemctl start httpd
systemctl enable httpd

echo "<h1>Hello World from EC2</h1>" > /var/www/html/index.html
