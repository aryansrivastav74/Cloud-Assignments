from flask import Flask, jsonify, render_template
import time
import datetime
import csv
import threading

app = Flask(__name__)

START_TIME = time.time()
SESSION_ID = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

cpu_samples = []
mem_samples = []
MAX_SAMPLES = 300
LOG_FILE = "system_metrics_log.csv"


def read_cpu_times():
    with open("/proc/stat") as f:
        for line in f:
            if line.startswith("cpu "):
                return list(map(int, line.split()[1:]))
    return [0] * 10


prev_cpu = read_cpu_times()


def get_cpu_metrics():
    global prev_cpu

    time.sleep(0.05)
    curr_cpu = read_cpu_times()

    prev_idle = prev_cpu[3] + prev_cpu[4]
    curr_idle = curr_cpu[3] + curr_cpu[4]

    prev_total = sum(prev_cpu)
    curr_total = sum(curr_cpu)

    total_diff = curr_total - prev_total
    idle_diff = curr_idle - prev_idle

    cpu_percent = (
        (total_diff - idle_diff) / total_diff * 100
        if total_diff > 0 else 0.0
    )

    cpu_samples.append(cpu_percent)
    if len(cpu_samples) > MAX_SAMPLES:
        cpu_samples.pop(0)

    usage_seconds = curr_total / 100
    prev_cpu = curr_cpu

    return {
        "current_percent": round(cpu_percent, 2),
        "average_percent": round(sum(cpu_samples) / len(cpu_samples), 2),
        "max_percent": round(max(cpu_samples), 2),
        "min_percent": round(min(cpu_samples), 2),
        "usage_seconds": round(usage_seconds, 2),
        "throttled_seconds": 0.0,
        "cpu_limit": "Local Machine"
    }


def get_memory_metrics():
    meminfo = {}
    with open("/proc/meminfo") as f:
        for line in f:
            key, value = line.split(":")
            meminfo[key] = int(value.strip().split()[0])

    total_kb = meminfo.get("MemTotal", 0)
    available_kb = meminfo.get("MemAvailable", 0)
    used_kb = total_kb - available_kb

    used_mb = used_kb / 1024
    total_mb = total_kb / 1024
    available_mb = available_kb / 1024

    percent = (used_mb / total_mb) * 100 if total_mb > 0 else 0

    mem_samples.append(percent)
    if len(mem_samples) > MAX_SAMPLES:
        mem_samples.pop(0)

    return {
        "current_percent": round(percent, 2),
        "used_mb": round(used_mb, 2),
        "available_mb": round(available_mb, 2),
        "limit_mb": round(total_mb, 2),
        "average_percent": round(sum(mem_samples) / len(mem_samples), 2),
        "max_percent": round(max(mem_samples), 2),
        "min_percent": round(min(mem_samples), 2)
    }


def initialize_session():
    with open(LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([])
        writer.writerow(["=" * 60])
        writer.writerow([f"Session Start: {SESSION_ID}"])
        writer.writerow(["=" * 60])
        writer.writerow([
            "timestamp",
            "uptime_seconds",
            "cpu_current",
            "cpu_average",
            "cpu_max",
            "cpu_min",
            "cpu_usage_seconds",
            "memory_current",
            "memory_used_mb",
            "memory_available_mb",
            "memory_limit_mb",
            "memory_average",
            "memory_max",
            "memory_min"
        ])


def log_metrics_periodically():
    while True:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        uptime_seconds = int(time.time() - START_TIME)

        cpu = get_cpu_metrics()
        memory = get_memory_metrics()

        with open(LOG_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                timestamp,
                uptime_seconds,
                cpu["current_percent"],
                cpu["average_percent"],
                cpu["max_percent"],
                cpu["min_percent"],
                cpu["usage_seconds"],
                memory["current_percent"],
                memory["used_mb"],
                memory["available_mb"],
                memory["limit_mb"],
                memory["average_percent"],
                memory["max_percent"],
                memory["min_percent"]
            ])

        time.sleep(30)


initialize_session()
threading.Thread(target=log_metrics_periodically, daemon=True).start()


@app.route("/")
def home():
    return "Hello from Cloud Run! System check complete."


@app.route("/analyze")
def analyze():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    uptime_seconds = int(time.time() - START_TIME)

    cpu_metric = get_cpu_metrics()
    memory_metric = get_memory_metrics()

    score = 100 - (
        cpu_metric["current_percent"] * 0.4 +
        memory_metric["current_percent"] * 0.4
    )
    health_score = max(0, min(100, int(score)))

    message = (
        "System is healthy and running optimally."
        if health_score >= 80 else
        "System is stable but under moderate load."
        if health_score >= 50 else
        "System is under high load and needs attention."
    )

    return jsonify({
        "timestamp": timestamp,
        "uptime_seconds": uptime_seconds,
        "cpu_metric": cpu_metric,
        "memory_metric": memory_metric,
        "health_score": health_score,
        "message": message
    })


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
