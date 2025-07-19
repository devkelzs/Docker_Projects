
### 📁 Project Structure

```
Docker_project5/
├── app/
│   ├── app.py               # Flask app logic
│   └── requirements.txt     # Python dependencies
├── Dockerfile               # Builds Flask app container
└── docker-compose.yml       # Defines multi-container stack
```

---

### 🧠 What This Project Does

* Runs a simple Python Flask app.
* Uses Redis as a data store to count visits.
* Sets up both services via Docker Compose.
* Services communicate over a shared Docker network.

---

### 🛠 Prerequisites

* [Docker Desktop](https://www.docker.com/products/docker-desktop) installed and running.
* WSL 2 integration enabled (for Windows users).
* `docker compose` or `docker-compose` command available.

---

### 🚀 How to Run the App

1. Open a terminal and navigate to the project directory:

   ```bash
   cd ~/Docker_Projects/Docker_project5
   ```

2. Run the containers:

   ```bash
   docker-compose up --build
   ```
  ![Alt Text](images/Screenshot%20(167).png)


3. Visit the app in your browser:

   [http://localhost:5000](http://localhost:5000)

   Refresh the page to increase the visit counter.
    ![Alt Text](images/Screenshot%20(166).png)
---

### 📋 Useful Docker Commands

| Command                  | Description                |
| ------------------------ | -------------------------- |
| `docker compose up`      | Start containers           |
| `docker compose down`    | Stop and remove containers |
| `docker compose logs -f` | View live logs             |
| `docker compose ps`      | List running services      |

---
![Alt Text](images/Screenshot%20(165).png)
  