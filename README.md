# Task 3 - Docker Containerization

A containerized Flask application demonstrating Docker containerization, PostgreSQL integration, CI/CD automation, Linux server administration, Nginx reverse proxy configuration, cloud deployment, health monitoring, and uptime monitoring.

---

## Project Overview

This project demonstrates the complete DevOps workflow for deploying a Flask web application using Docker and cloud infrastructure.

### Main Technologies

- Python
- Flask
- PostgreSQL
- Docker
- Docker Compose
- Gunicorn
- GitHub Actions
- Nginx
- Linux
- UFW
- Render
- UptimeRobot

---

# Application

The application is built using Flask and provides a simple web endpoint along with database-related functionality.

### Application Endpoints

| Endpoint | Purpose |
|----------|---------|
| `/` | Application status |
| `/health` | Application and database health check |
| `/visit` | Visit-related functionality |
| `/visits` | Visit information |

The root endpoint `/` is used as the Render HTTP health-check endpoint because it does not require an external database connection.

---

# Docker Containerization

The application is packaged using Docker.

### Docker Features

- Python 3.12 Alpine base image
- Lightweight container
- Non-root application user
- Gunicorn application server
- Docker health check
- Exposed application port 5000
- Reduced image size

### Docker Build

```bash
docker build -t task3-web .
```

### Run Docker Container

```bash
docker run -p 5000:5000 task3-web
```

Application:

```text
http://localhost:5000
```

---

# Docker Compose

Docker Compose is provided for running the Flask application together with PostgreSQL.

### Start Services

```bash
docker compose up -d
```

### Check Services

```bash
docker compose ps
```

### Stop Services

```bash
docker compose down
```

The PostgreSQL database uses a persistent Docker volume so that database data can be retained between container restarts.

---

# Docker Health Check

The Docker container includes a health check for the application root endpoint.

```dockerfile
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://127.0.0.1:5000/ || exit 1
```

The root endpoint returns the current application status.

---

# CI/CD Pipeline

GitHub Actions is configured to automate the development pipeline.

The workflow performs:

1. Source code checkout
2. Python environment setup
3. Dependency installation
4. Code linting
5. Unit testing
6. Docker image build
7. GitHub Container Registry authentication
8. Docker image push on the main branch

### Pipeline

```text
GitHub Repository
        |
        v
GitHub Actions
        |
        v
Install Dependencies
        |
        v
Linting
        |
        v
Unit Tests
        |
        v
Docker Build
        |
        v
GitHub Container Registry
```

---

# Linux Server Administration

Linux server administration and security configuration are documented in:

```text
LINUX_SERVER_SETUP.md
```

The documentation covers:

- Dedicated non-root administration user
- SSH key authentication
- Password-based SSH disabled
- Root SSH login disabled
- UFW firewall configuration
- Required ports
- Nginx configuration
- SSL/TLS configuration
- Service verification

### Required Firewall Ports

| Port | Purpose |
|------|---------|
| 22 | SSH |
| 80 | HTTP |
| 443 | HTTPS |

---

# Nginx Reverse Proxy

The project includes:

```text
nginx.conf
```

The Nginx configuration demonstrates:

- Reverse proxy
- Gzip compression
- Cache-Control headers
- Request rate limiting
- Forwarded request headers

### Architecture

```text
Client
   |
   v
Nginx :80/:443
   |
   v
Flask Application :5000
```

For production deployment, HTTPS can be configured using Let's Encrypt Certbot.

---

# Cloud Deployment

The containerized application is deployed on Render using a Docker Web Service.

### Deployment Details

| Configuration | Value |
|---------------|-------|
| Platform | Render |
| Runtime | Docker |
| Service | task3-docker-app |
| Region | Singapore |
| Branch | main |
| Plan | Free |

---

# Live Application

The application is publicly available at:

https://task3-docker-app.onrender.com

### Current Application Response

```json
{
  "project": "Task 3 - Docker Containerization",
  "status": "running"
}
```

---

# Environment Configuration

Production environment configuration is managed through Render Environment Variables.

```text
APP_ENV=production
```

This separates deployment environment configuration from the application source code.

---

# Cloud Health Monitoring

Render health monitoring is configured for the root endpoint:

```text
/
```

The endpoint returns a successful HTTP response when the application is running.

The health check helps verify that the deployed container is responding correctly.

---

# Uptime Monitoring

The live cloud application is monitored using UptimeRobot.

### Monitor Details

```text
Monitor Name: Task 6 Cloud Application
Monitor Type: HTTP(s)
URL: https://task3-docker-app.onrender.com
Status: Up
```

The monitor periodically checks the live application and records uptime and response-time information.

---

# Cloud Deployment Architecture

```text
                    GitHub Repository
                           |
                           v
                    GitHub Actions
                           |
                           v
                    Docker Build
                           |
                           v
                    Render Cloud
                           |
                           v
                   Docker Container
                           |
                           v
                       Gunicorn
                           |
                           v
                    Flask Application
                           |
                           v
                    HTTP Health Check
                           |
                           v
                    Uptime Monitoring
```

---

# End-to-End Deployment Pipeline

```text
Developer
    |
    v
GitHub Repository
    |
    v
GitHub Actions
    |
    +--> Linting
    |
    +--> Unit Testing
    |
    +--> Docker Build
    |
    v
Render Cloud Deployment
    |
    v
Docker Container
    |
    v
Live Flask Application
    |
    +--> Health Check
    |
    +--> Uptime Monitoring
```

---

# Project Structure

```text
task3-docker-containerization/
│
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── nginx.conf
├── LINUX_SERVER_SETUP.md
├── README.md
│
└── .github/
    └── workflows/
        ├── docker-ci.yml
        └── ci-cd.yml
```

---

# Verification Commands

### Check Docker Image

```bash
docker images
```

### Check Running Containers

```bash
docker ps
```

### Test Application

```bash
curl http://localhost:5000/
```

### Validate Nginx Configuration

```bash
sudo nginx -t
```

### Check UFW

```bash
sudo ufw status
```

### Check Nginx Service

```bash
sudo systemctl status nginx
```

---

# Task 2 - Service Blueprint and Cloud Cost Model

The project planning phase included:

- Service blueprint
- SLO definitions
- Cloud cost model
- Architecture decision records
- Cost and reliability trade-off analysis

---

# Task 3 - Docker Containerization

Implemented:

- Flask application containerization
- PostgreSQL container
- Docker Compose
- Persistent database volume
- Docker health check
- Non-root container user
- Optimized Docker image

---

# Task 4 - CI/CD

Implemented GitHub Actions workflows for:

- Automated testing
- Linting
- Docker image building
- Container registry integration

---

# Task 5 - Linux Server Administration and Nginx

Implemented documentation and configuration for:

- Linux user administration
- SSH key authentication
- UFW firewall
- Nginx reverse proxy
- Gzip compression
- Cache-Control headers
- Rate limiting
- SSL/TLS configuration

---

# Task 6 - Cloud Infrastructure Deployment and Monitoring

Implemented:

- Docker-based cloud deployment on Render
- Production environment variable configuration
- HTTP health check
- Live cloud endpoint
- Uptime monitoring
- Deployment architecture documentation
- End-to-end deployment pipeline documentation

---

# Final Project Status

```text
Docker Containerization       : Completed
Docker Compose                : Completed
CI/CD Configuration           : Completed
Linux Server Documentation    : Completed
Nginx Configuration           : Completed
Cloud Deployment              : Completed
Environment Configuration     : Completed
Health Monitoring             : Completed
Uptime Monitoring             : Completed
```

---

# Live Endpoint

https://task3-docker-app.onrender.com

# GitHub Repository

https://github.com/vyuvansankarraja/task3-docker-containerization
