Form Data Collection & Cloud Storage Application

Overview

A Django-based web application that collects user registration data, performs strong backend validation, and securely stores records. The project is deployed on a Google Cloud Virtual Machine with proper firewall and host configuration.

Features

Form validation with secure input handling

Unique email verification

Strong password policy enforcement

Data storage in SQLite and CSV

Deployment on Google Cloud VM

🛠 Tech Stack

Backend: Django (Python)

Frontend: HTML, CSS

Database: SQLite

Hosting: Google Cloud VM

Environment: Linux (Debian)

🔄 Application Workflow

User submits registration form

Backend validates input

Email duplication check performed

Password strength verified

Data stored securely

Success response displayed

📂 Project Structure
formproject/
│
├── formapp/
├── static/
├── db.sqlite3
├── user_data.csv
└── manage.py

⚙ Deployment Details

Server: Google Cloud VM

Port: 8000

Firewall: Ingress rule enabled

ALLOWED_HOSTS configured for external access

▶ How to Run

Activate virtual environment

source gcp-venv/bin/activate


Navigate to project

cd formproject


Apply migrations

python manage.py migrate


Start server

python manage.py runserver 0.0.0.0:8000


Access in browser

(http://35.197.112.48:8000/)

🎯 Learning Outcomes

Django form handling

Backend validation logic

Cloud VM deployment

Firewall configuration

Author
Aryan Srivastava

Project SnapShot :
<img width="1919" height="908" alt="user" src="https://github.com/user-attachments/assets/172db674-535f-484d-9dfc-a57d159b1094" />
