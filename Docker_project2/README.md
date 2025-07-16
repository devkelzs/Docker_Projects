# 🌐 Dockerized Static Website

This project serves a simple static HTML/CSS website using **Nginx** inside a **Docker container**.

---

## 📁 Project Structure

```

static-website/
├── Dockerfile
└── website/
├── index.html
└── style.css

````

---

## 🚀 How to Run This Project

### 1️⃣ Clone the Repository *(if applicable)*

```bash
git clone https://github.com/your-username/static-website.git
cd static-website
````

### 2️⃣ Build the Docker Image

```bash
docker build -t website-static .
```

### 3️⃣ Run the Docker Container

Run on port `8080` (or another if 8080 is in use):

```bash
docker run -d -p 8080:80 website-static
```

Access the site in your browser:

```
http://localhost:8080
```

---

## 📦 Dockerfile Explanation

```Dockerfile
FROM nginx:alpine                  # Use lightweight Nginx image
RUN rm -rf /usr/share/nginx/html/* # Remove default page
COPY website/ /usr/share/nginx/html/ # Copy static files into container
EXPOSE 80                          # Expose port 80
```

---







