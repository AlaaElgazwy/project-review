

# 🧮 Django Smart Calculator

A modern, web-based calculator application built with **Python Django** and styled with **CSS Grid**. This project demonstrates a full **DevOps lifecycle**, including containerization with **Docker** and automated CI/CD pipelines using **Jenkins**.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-4.0%2B-green)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-red)

## 🌟 Features
- **Backend Logic**: Mathematical operations handled securely via Python views.
- **Modern UI**: Responsive design using CSS Grid and Flexbox.
- **Error Handling**: Graceful handling of division by zero and invalid inputs.
- **Containerized**: Fully Dockerized for consistent environments.
- **Automated**: Jenkins pipeline for building and pushing images to Docker Hub.

---

## 🛠️ Tech Stack
- **Framework**: Django (Python)
- **Frontend**: HTML5, CSS3
- **Containerization**: Docker & Docker Compose
- **CI/CD**: Jenkins

---

## 🚀 How to Run Locally (Without Docker)

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/AlaaElgazwy/project-review.git](https://github.com/AlaaElgazwy/project-review.git)
   cd project-review

    Create a Virtual Environment:
    Bash

    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate

    Install Dependencies:
    Bash

    pip install -r requirements.txt

    Run the Server:
    Bash

    python manage.py runserver

    Open your browser at http://127.0.0.1:8000.

🐳 How to Run with Docker

You don't need to install Python or Django on your machine if you have Docker.

    Build and Run:
    Bash

    docker-compose up --build

    Access the App: Go to http://localhost:8000 in your browser.

    Stop the Container: Press Ctrl+C or run:
    Bash

    docker-compose down

⚙️ Jenkins CI/CD Pipeline

This project includes a Jenkinsfile that automates the deployment process.
Pipeline Stages:

1. Checkout: Pulls the latest code from GitHub.
2. Build: Creates a Docker image based on the Dockerfile.
3. Login: Authenticates with Docker Hub securely using Jenkins Credentials
4. Push: Pushes the production-ready image to Docker Hub.


open https://django-calculator-latest.onrender.com


