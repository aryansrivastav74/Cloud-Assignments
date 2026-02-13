# Form Data Collection & Cloud Storage App

A secure, cloud-deployed registration engine.

---

## 1. Project Overview
This application provides a secure registration pipeline hosted on a Google Cloud VM. It bridges the gap between front-end data collection and secure back-end persistence using Django's robust validation framework.

---

## 2. Tech Stack
* Backend: Django (Python 3.x)
* Frontend: HTML5 & CSS3
* Database: SQLite (Primary) & CSV (Backup)
* Infrastructure: Google Cloud VM (Debian)
* Networking: GCE Firewall, Port 8000

---

## 3. Key Features
* Strong Backend Validation: Leverages Django `forms.py` to prevent XSS and malformed data.
* Unique Email Verification: Logic to ensure no duplicate accounts can be created.
* Password Complexity: Enforces strict security policies at the entry point.
* Dual-Storage Engine: Simultaneously writes to a relational DB and a flat-file CSV.
* Cloud Deployment: Fully configured for external access via GCP Ingress rules.

---

<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/eb03c57c-8f8c-4c7a-acac-33aeef2f7188" />

---

## 5. Application Workflow
* Submission: User inputs data into the registration form via the frontend interface.
* Validation:
    * Checks for empty or malformed fields.
    * Verifies email uniqueness against existing database records.
    * Tests password entropy to ensure high security.
* Persistence: Validated records are securely stored in `db.sqlite3` and simultaneously appended to `user_data.csv`.
* Response: A real-time success message is triggered via the Django Messages framework to confirm registration.

---

## 6. Deployment Details
* Server Infrastructure: Hosted on Google Cloud Platform (GCP) using a Debian Linux VM.
* Networking: Configured with a specific Ingress Firewall Rule to allow traffic on TCP Port 8000.
* Host Configuration: `ALLOWED_HOSTS` is strictly defined to include the static IP `35.197.112.48` and `localhost` for secure access.

---

## 7. How to Run

Step 1: Activate Environment
source gcp-venv/bin/activate

Step 2: Install Dependencies
pip install -r requirements.txt

Step 3: Migrate & Run
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

---

## 8. Author
* Name: Aryan Srivastava


## 9. Project Snapshot

<img width="1919" height="908" alt="user" src="https://github.com/user-attachments/assets/c4d14269-5073-46ed-b65e-4e275f04f99f" />
