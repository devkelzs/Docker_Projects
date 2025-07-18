
# 🐳 Docker Volumes for Persistent Logs

## 🧠 Goal
Demonstrate how to use Docker **volumes** and **bind mounts** to persist data outside of a container — even after the container stops or is deleted.

---

## 📁 Project Structure



docker-volume-demo/
│
├── Dockerfile
├── app.py
├── logs/                # (Create only if using bind mount)
└── README.md



---

## 📦 What This Project Does

This project includes a simple Python script that:
- Writes logs to a file every second.
- Outputs the log file to a persistent volume (either a bind mount or a Docker volume).

---

## 🛠️ How to Use This Project

### ✅ 1. Clone or Create Folder


### ✅ 2. Create `app.py`

```python
import time
import os

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

with open("logs/output.log", "a") as f:
    for i in range(5):
        f.write(f"Log entry {i} at {time.ctime()}\n")
        time.sleep(1)
```

---

### ✅ 3. Create `Dockerfile`

```Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]
```

---

### ✅ 4. Build Docker Image

```bash
docker build -t log-writer .
```

---

## 🧪 Option 1: Use Bind Mount (Recommended for local dev)

### 🪵 Create a Local Logs Folder

```bash
mkdir logs
```

### ▶️ Run Container with Bind Mount

```bash
docker run --name mylogger -v $(pwd)/logs:/app/logs log-writer
```

### 📄 View Logs on Host

```bash
cat logs/output.log
```

---

## 🧪 Option 2: Use Docker Named Volume

### 📦 Create Docker Volume

```bash
docker volume create mylogvolume
```

### ▶️ Run Container with Named Volume

```bash
docker run --name mylogger -v mylogvolume:/app/logs log-writer
```

### 🔍 Inspect Volume

```bash
docker volume inspect mylogvolume
```

### 🧾 Read Log Using Helper Container

```bash
docker run --rm -v mylogvolume:/data alpine cat /data/output.log
```

---

## 🔁 Re-run to Test Persistence

After removing and re-running the container:

```bash
docker rm mylogger

# Run again (choose the same volume or mount)
docker run --name mylogger -v $(pwd)/logs:/app/logs log-writer
```

You’ll notice that **new logs are appended** to the same `output.log`.

---

## 🧰 Docker Commands Summary

| Task                  | Command                                                            |
| --------------------- | ------------------------------------------------------------------ |
| Build image           | `docker build -t log-writer .`                                     |
| Create volume         | `docker volume create mylogvolume`                                 |
| Run with bind mount   | `docker run -v $(pwd)/logs:/app/logs log-writer`                   |
| Run with named volume | `docker run -v mylogvolume:/app/logs log-writer`                   |
| Inspect volume        | `docker volume inspect mylogvolume`                                |
| Read logs (volume)    | `docker run --rm -v mylogvolume:/data alpine cat /data/output.log` |

---







