# Deploying a Flask + PostgreSQL App on AWS (EC2 + RDS + Nginx)

This project demonstrates how to build, deploy, and secure a full-stack web application on AWS using:

- **Flask** for backend APIs
- **PostgreSQL** (Amazon RDS) for managed database
- **Nginx** as a reverse proxy and static file server
- **EC2** for application hosting
- **Security Groups** for controlled network access

## 🛠️ Technologies Used

- **AWS EC2** – Compute for frontend & backend
- **AWS RDS (PostgreSQL)** – Managed relational database
- **Flask** – Backend REST API
- **Nginx** – Reverse proxy & static web server
- **DBeaver** – Database client
- **SQLAlchemy** – Database interaction
- **HTML, CSS, JavaScript** – Frontend UI

## 📌 Phase 1: Database Setup (RDS PostgreSQL)
### 1. Create RDS Instance
Engine: **PostgreSQL**
Free-tier eligible
Public access: **Enabled** (initially for local development)
Port: 5432

### 2. Configure Security Group (Local Development)
Inbound rule:

````
PostgreSQL (5432) → 0.0.0.0/0 (everywhere)
````
This allows:
- Connection from **DBeaver**
- CRUD operations from local Flask app

## 🧪 Phase 2: Local Development & Testing
### Database Access

Connected to RDS using **DBeaver**

Created table:
````
CREATE TABLE events (
  id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  title VARCHAR(100),
  description VARCHAR(100)
);
````

### Backend (Flask)

Implemented CRUD APIs:

- **GET** /events
- **POST** /events
- **DELETE** /events/{id}

Verified operations from local machine

## ☁️ Phase 3: EC2 Deployment
### 1. Launch EC2 Instance

- Amazon Linux
- Free-tier eligible
- Security Group
````
Inbound rule:
HTTP (80) → Public IP of My Machine
````
- Connect to instance from AWS console

### 2. Install Required Packages
````
sudo yum update -y
sudo yum install python3 nginx -y
````

## 🔐 Phase 4: Securing RDS Access (Best Practice)
**Initial State**
- RDS accessible from local machine (CIDR-based rule)

**Final Secure Setup**
- Removed public CIDR rule
- Added inbound rule to RDS security group:

````
PostgreSQL (5432) → EC2 Security Group
````

**Benefits**
- Database not exposed to the internet
- Only EC2 backend can connect

## 🌐 Phase 5: Frontend + Backend Integration (Nginx)
Nginx Responsibilities

- Serve index.html (frontend)
- Proxy API calls to Flask backend

**Nginx Configuration**
````
server {
    listen 80;
    server_name _;

    location / {
        root /usr/share/nginx/html;
        index index.html;
    }

    location /api {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
````
**Result**
- Frontend accessed via:
````
http://EC2_PUBLIC_IP
````

## 🔑 Best Practices

- Always use SG → SG instead of IP CIDR
- Keep RDS not publicly accessible
- Separate SGs for App and DB
- Least privilege (only DB port allowed)
- SG reference works only within connected VPCs