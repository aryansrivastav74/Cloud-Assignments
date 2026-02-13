# System Health Monitoring App (Cloud Run)

A Flask-based System Health Monitoring application designed for cloud-native deployment on Google Cloud Run. This tool provides real-time CPU and memory metrics, calculates system health scores, and logs performance via a background process.

---

## Project Overview
This application demonstrates cloud-native development by interfacing directly with Linux system files to monitor performance.

* Real-time Monitoring: Tracks CPU and Memory usage via /proc/stat and /proc/meminfo.
* Health Logic: Calculates a dynamic health score based on resource consumption.
* Dual Interface: Exposes data via a JSON API and a visual Dashboard.
* Background Processing: Implements threading for continuous CSV logging.

---

## Technology Stack

* Backend: Python (Flask)
* OS Level: Linux System Files (/proc)
* Frontend: HTML5, CSS3
* Deployment: Google Cloud Run
* Logging: CSV & Background Threading

---

## Application Architecture
<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/a39add3b-5905-4060-8105-27a879d6715b" />


## Application Routes

### 1. Home Route (/)
Purpose: Acts as a health check endpoint to verify the container is running.
* Response: Simple text confirmation.

<img width="1258" height="452" alt="Screenshot 2026-02-13 2 50 45 PM" src="https://github.com/user-attachments/assets/ef127857-5351-4d7d-81ef-36c8bee88905" />


### 2. Analyze Route (/analyze)
Purpose: Returns raw data and calculated metrics in structured JSON.
* Metrics: Current/Avg/Min/Max for CPU & Memory, Uptime, and Health Score.

<img width="1247" height="580" alt="analyze" src="https://github.com/user-attachments/assets/9c898dc5-a0e7-4024-b71a-04a00bb9ee79" />


### 3. Dashboard Route (/dashboard)
Purpose: A user-friendly HTML interface to visualize system status.

<img width="1919" height="956" alt="dashboard" src="https://github.com/user-attachments/assets/6e9a2e4c-328d-42c6-8a2f-cf54b75359fc" />


---

## Health Score Logic

The application calculates a composite score to determine system stability:

Health Score = 100 - (CPU% * 0.4 + Memory% * 0.4)

### Status Levels
| Score Range | Status | Description |
| :--- | :--- | :--- |
| 80 – 100 | Healthy | Optimal performance |
| 50 – 79 | Moderate | Standard load |
| < 50 | High Load | System under stress |

---

## How to Run

### Local Development

1. Create Virtual Environment
python3 -m venv venv

2. Activate Environment
source venv/bin/activate

3. Install Dependencies
pip install flask

4. Run Application
python main.py

* Access at: http://localhost:8080

### Cloud Run Deployment Notes
* Port: Application listens on 8080.
* Host: Configured to 0.0.0.0 for external access.
* State: Designed as a stateless container.

---

## Learning Outcomes
* Flask multi-route architecture.
* Linux system-level monitoring without external libraries.
* Python background threading for non-blocking logging.
* REST API design principles.
* Cloud Run deployment and debugging.

---

## Future Enhancements
* [ ] Migrate logging to BigQuery or Cloud Storage.
* [ ] Add real-time charts using JavaScript (Chart.js).
* [ ] Implement API Authentication.
* [ ] Set up automated alerting mechanisms.

---

## Author
Aryan Srivastava

