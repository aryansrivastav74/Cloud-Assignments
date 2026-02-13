System Health Monitoring Application
Overview

A Flask-based web application that monitors real-time CPU and memory usage, calculates a system health score, and logs metrics periodically into a CSV file. Designed to run on a Virtual Machine or Cloud Run.

Features

Real-time CPU monitoring

Real-time memory monitoring

Health score calculation

REST API endpoint (/analyze)

Background logging every 30 seconds

CSV-based metrics storage

Web dashboard interface

Tech Stack

Python 3

Flask

Linux system files (/proc/stat, /proc/meminfo)

CSV

Threading

API Endpoints

/ – Basic system response

/analyze – Returns system metrics in JSON

/dashboard – Renders monitoring dashboard

Health Score Logic
Health Score = 100 - (CPU × 0.4 + Memory × 0.4)


≥ 80: Healthy

50–79: Moderate Load

< 50: High Load

Run Instructions

Activate virtual environment

source gcp-venv/bin/activate


Install dependencies

pip install flask


Run application

python app.py


Access

http://<EXTERNAL_IP>:8080

Author

Aryan Srivastava
