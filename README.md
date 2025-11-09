# 🚀 Docker Build & Push Pipeline

This repository contains a GitHub Actions workflow that **automatically builds a Docker image** from your code and **pushes it to Docker Hub** under your account (`your_docker_hub_name`).

---

## ⚙️ Features

- ✅ Automatic Docker image build on every push to `main`
- ✅ Pushes image to Docker Hub: `your_docker_hub_name/<repository-name>:latest`
- ✅ Repository name automatically lowercased for valid Docker tags
- ✅ Manual trigger supported (via “Run workflow” button in GitHub UI)

---

## 🧩 Requirements

1. **Dockerfile** — must exist in the root directory of the repository  
2. **Docker Hub account** — create one at [https://hub.docker.com](https://hub.docker.com)
3. **GitHub Secrets** — add your Docker Hub credentials to the repository:

   | Secret Name | Value |
   |--------------|-------|
   | `DOCKERHUB_USERNAME` | Your Docker Hub username (`your_docker_hub_name`) |
   | `DOCKERHUB_TOKEN` | Docker Hub Access Token (from [Docker Hub → Account Settings → Security](https://hub.docker.com/settings/security)) |

---

## 🧠 How It Works

The workflow is defined in:
