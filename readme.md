# CI/CD Pipeline for Flask Application using GitHub Actions, Docker, AWS ECR and EC2

## Project Overview

This project demonstrates a complete CI/CD pipeline using GitHub Actions.

The pipeline automatically:

1. Checks out source code from GitHub
2. Installs Python dependencies
3. Runs automated tests using Pytest
4. Builds a Docker image
5. Tags the image using the Git Commit SHA
6. Pushes the image to Amazon Elastic Container Registry (ECR)
7. Deploys the latest image to an AWS EC2 instance
8. Verifies deployment using a health check endpoint
9. Sends email notifications for successful and failed deployments

---

## Architecture

```text
Developer Push
      |
      v
GitHub Repository
      |
      v
GitHub Actions
      |
      +--> Install Dependencies
      |
      +--> Run Pytest
      |
      +--> Build Docker Image
      |
      +--> Push Image to Amazon ECR
      |
      +--> Deploy to EC2
      |
      +--> Health Check Verification
      |
      +--> Email Notification
```

---

## Project Structure

```text
CICD/
│
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── README.md
│
└── .github/
    └── workflows/
        └── cicd.yml
```

---

## Application Details

### Home Endpoint

```http
GET /
```

Response:

```text
Hello from CI/CD Pipeline!
```

### Health Endpoint

```http
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

The health endpoint is used by the deployment verification step to ensure the application is running successfully after deployment.

---

## Technologies Used

- Python 3.11
- Flask
- Pytest
- Docker
- GitHub Actions
- AWS ECR
- AWS EC2
- IAM Roles
- Gmail SMTP Notifications

---

## AWS Resources Used

### Amazon ECR

Repository:

```text
cicd-flask-app
```

Repository URI:

```text
356042515069.dkr.ecr.us-east-1.amazonaws.com/cicd-flask-app
```

### EC2 Instance

Instance Name:

```text
CICD
```

Public IP:

```text
54.165.69.62
```

IAM Role:

```text
AmazonEC2ContainerRegistryReadOnly
```

Region:

```text
us-east-1
```

---

## EC2 Configuration

### Install Docker

```bash
sudo yum update -y

sudo yum install docker -y

sudo systemctl enable docker

sudo systemctl start docker

sudo usermod -aG docker ec2-user
```

Verify:

```bash
docker --version
```

---

## Local Setup

### Clone Repository

```bash
git clone https://github.com/Snehap2907/CICD-pipeline-assignment.git

cd CICD-pipeline-assignment
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Application URL:

```text
http://localhost:5000
```

Health Check:

```text
http://localhost:5000/health
```

---

## Running Tests

Execute:

```bash
pytest
```

Expected Output:

```text
2 passed
```

---

## Docker Commands

### Build Image

```bash
docker build -t flask-app .
```

### Run Container

```bash
docker run -d -p 5000:5000 flask-app
```

### Verify

```bash
curl http://localhost:5000/health
```

---

## GitHub Actions Workflow

Workflow file:

```text
.github/workflows/cicd.yml
```

Pipeline stages:

### 1. Checkout

Downloads latest source code.

### 2. Install Dependencies

Installs packages from:

```text
requirements.txt
```

### 3. Test

Runs:

```bash
pytest
```

Pipeline stops if tests fail.

### 4. Build

Builds Docker image.

### 5. Push

Pushes image to Amazon ECR.

### 6. Deploy

Connects to EC2 via SSH and:

- Pulls latest image
- Stops existing container
- Removes old container
- Starts new container

### 7. Verify

Runs health check:

```bash
curl http://localhost:5000/health
```

### 8. Notify

Sends email notification indicating success or failure.

---

## GitHub Secrets Configuration

The following secrets must be configured under:

```text
Repository
→ Settings
→ Secrets and Variables
→ Actions
```

### AWS

```text
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
```

### ECR

```text
ECR_REPOSITORY
```

### EC2

```text
EC2_HOST
EC2_USER
EC2_SSH_KEY
```

### Email

```text
EMAIL_USERNAME
EMAIL_PASSWORD
EMAIL_TO
```

---

## Deployment Strategy

The deployment uses SSH-based deployment.

GitHub Actions connects to the EC2 instance using a private SSH key stored securely as a GitHub Secret.

Deployment steps:

1. SSH into EC2
2. Login to Amazon ECR
3. Pull latest Docker image
4. Stop existing container
5. Remove old container
6. Start new container
7. Verify health endpoint

This approach provides a simple and reliable deployment mechanism for a single EC2 instance.

---

## Manual Deployment Procedure

If GitHub Actions is unavailable, deployment can be performed manually.

### Login to EC2

```bash
ssh -i SnehaKey.pem ec2-user@54.165.69.62
```

### Login to ECR

```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 356042515069.dkr.ecr.us-east-1.amazonaws.com
```

### Pull Latest Image

```bash
docker pull 356042515069.dkr.ecr.us-east-1.amazonaws.com/cicd-flask-app:latest
```

### Stop Existing Container

```bash
docker stop flask-app
docker rm flask-app
```

### Run New Container

```bash
docker run -d \
--name flask-app \
-p 5000:5000 \
356042515069.dkr.ecr.us-east-1.amazonaws.com/cicd-flask-app:latest
```

### Verify Deployment

```bash
curl http://localhost:5000/health
```

Expected Response:

```json
{
  "status": "ok"
}
```

---

## Screenshots to Include in Submission

### Successful Pipeline Run

Capture:

- Checkout
- Test
- Build
- Push
- Deploy
- Success Notification

### Successful Email

Include received success email.

### Failed Pipeline Run

Introduce a failing test intentionally and capture:

- Pipeline failure
- Failed stage details

### Failure Email

Include received failure email.

---

## Repository Link

```text
https://github.com/Snehap2907/CICD-pipeline-assignment
```

---

## Author

Sneha Pandey

CI/CD Pipeline Assignment using:

- GitHub Actions
- Docker
- AWS ECR
- AWS EC2
- Flask
- Pytest