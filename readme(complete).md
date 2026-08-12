## 📂 Project Path & Structure

E:\Download\CICDFlask/
│
├── app.py                # Flask app (with /health route added)
├── requirements.txt      # Python dependencies
├── test_app.py           # Pytest unit tests
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── add_student.html
│   └── update_student.html
├── Dockerfile            # Docker build instructions
├── .dockerignore         # Ignore unnecessary files
├── .env.example          # Environment variable template
├── README.md             # Documentation
└── .github/
└── workflows/
└── ci-cd.yml     # GitHub Actions pipeline



---

## 🧱 Tech Stack
- **Python 3.9**
- **Flask**
- **MongoDB**
- **Docker**
- **AWS (ECR + EC2)**
- **GitHub Actions**

---

## ⚙️ Steps Followed

### 1️⃣ Fork & Clone
- Forked the repo: `github.com/mohanDevOps-arch/flask_Practice`
- Cloned locally into `E:\Download\CICDFlask`

### 2️⃣ Add Dockerfile
- Created a Dockerfile to run Flask on port 5000.
- Tagged images with **commit SHA**.

### 3️⃣ Add `/health` Route
- Implemented `/health` endpoint in `app.py` to check MongoDB connectivity.
- Used this as the **deployment verification gate**.

### 4️⃣ Provision AWS
- Created **ECR repository** for Docker images.
- Launched **EC2 instance** with Docker installed.
- Configured **IAM role** for ECR pull.
- Security group rules:  
  - Port **22** (SSH)  
  - Port **5000** (Flask app)

### 5️⃣ Write Pipeline
- Added **GitHub Actions workflow** (`ci-cd.yml`) with stages:
  1. Checkout  
  2. Install dependencies  
  3. Run tests (pytest)  
  4. Build Docker image  
  5. Push to ECR  
  6. Deploy to EC2  
  7. Verify `/health`  
  8. Notify via email

### 6️⃣ Configure Email Alerts
- Used `dawidd6/action-send-mail` for notifications.
- Customized success/failure messages with commit SHA and stage info.

### 7️⃣ Test End-to-End
- Pushed changes → pipeline triggered.
- Verified deployment on EC2.
- Received success and failure emails.

### 8️⃣ Document & Submit
- Updated README.md with setup, secrets, and deploy steps.
- Prepared screenshots of successful and failed runs.

---

## 📬 Secrets Configuration (GitHub → Settings → Secrets)
- `AWS_ACCOUNT_ID`
- `AWS_ECR_REPO`
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `EC2_PUBLIC_IP`
- `EC2_SSH_KEY`
- `SMTP_USER`
- `SMTP_PASS`
- `NOTIFY_EMAIL`

---

## 🧪 Health Check
After deployment, verify:


<img width="1827" height="972" alt="image" src="https://github.com/user-attachments/assets/377fd10d-d7bd-43dc-b93d-f1ab0f3e7e27" />

<img width="1023" height="422" alt="image" src="https://github.com/user-attachments/assets/65462608-60f1-47b0-8c70-517e5e6159d2" />

