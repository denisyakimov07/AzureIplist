# 🔍 Azure IP Extractor

Extract IPv4 addresses from any text and checks if they belong to **Microsoft Azure’s public IP ranges**.

---

## 🚀 Features

- 🧠 Extract all IPv4 addresses from arbitrary text input  
- ☁️ Validate if IPs exist in Azure’s published IP ranges  
- 🐳 **Docker**
---
## 🧩
- **Python 3.11+**
- **Streamlit**
---
## 📦 Installation: [DockerHUB](https://hub.docker.com/repository/docker/denisyakimov/azureiplist)
```bash
   docker run -d \
  --name azure-ip-extractor \
  -p 8501:8501 \
  -e STREAMLIT_SERVER_HEADLESS=true \
  -e STREAMLIT_SERVER_ENABLECORS=false \
  -e STREAMLIT_SERVER_ENABLEXSRSFPROTECTION=false \
  denisyakimov/azureiplist
```

