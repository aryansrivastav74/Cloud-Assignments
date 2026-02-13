📝 Form Data Collection & Cloud Storage App

A robust Django-based registration system designed with security and cloud scalability in mind. This application handles user data through a multi-layered validation pipeline and is deployed on a Google Cloud Platform (GCP) Compute Engine instance.

Overview

This project demonstrates a complete end-to-end workflow: from building a secure backend that prevents duplicate entries and enforces password entropy, to configuring a cloud-based Linux environment with specific firewall rules for public access.

🛠 Tech Stack

Backend: Django (Python 3.x)

Frontend: HTML5, CSS3

Database: SQLite (Relational) & CSV (Flat-file backup)

Infrastructure: Google Cloud VM (Debian Linux)

Networking: GCE Firewall, Virtualenv

⚙️ Key Features
Strong Backend Validation: Prevents XSS and injection by leveraging Django's native form handling.

Integrity Checks: Automated verification for unique email addresses to prevent account duplication.

Password Policy: Enforces complexity requirements to ensure user data security.

Dual-Layer Storage: Records are persisted in db.sqlite3 for the app and appended to user_data.csv for data portability.

Cloud Optimized: Specifically configured for remote hosting with ALLOWED_HOSTS and custom Ingress rules.

🔄 Application Workflow
Submission: User enters details via the HTML frontend.

Validation: Django forms check for data types and required fields.

Security Check: Backend runs duplication checks on the email and evaluates password strength.

Persistence: Upon passing validation, data is committed to both the SQL database and a local CSV file.

Response: User receives a success confirmation and a redirect.

📂 Project Structure
Plaintext

formproject/
│
├── formapp/            # Application logic, models, and views
├── static/             # CSS, JavaScript, and Images
├── db.sqlite3          # Relational database storage
├── user_data.csv       # Flat-file data backup
├── manage.py           # Django management script
└── requirements.txt    # Project dependencies
☁️ Deployment & Installation
1. Prerequisites
Ensure your Google Cloud Firewall allows traffic on Port 8000 for the target VM instance.

2. Setup
Bash
# Clone the repository
git clone <your-repo-link>
cd formproject

# Activate the virtual environment
source gcp-venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate
3. Execution
Bash
# Start the server on all network interfaces
python manage.py runserver 0.0.0.0:8000
Note: Access the live application at: http://35.197.112.48:8000/

🎯 Learning Outcomes
Django Internals: Mastering the forms.py and views.py relationship.

Security: Implementing server-side validation over client-side reliance.

Cloud Computing: Configuring Google Cloud Virtual Machines, static IPs, and firewall ingress rules.

Linux Administration: Managing Python environments and background processes via SSH.

Author: Aryan Srivastava
