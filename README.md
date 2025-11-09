# 🔍 Azure IP Extractor

A simple yet powerful **Streamlit web app** that extracts IPv4 addresses from any text and checks if they belong to **Microsoft Azure’s public IP ranges**.

---

## 🚀 Features

- 🧠 Extract all IPv4 addresses from arbitrary text input  
- ☁️ Validate if IPs exist in Azure’s published IP ranges  
- ⚡ Fast and cached lookups for better performance  
- 🌍 Download or link to the latest Microsoft IP JSON file automatically  
- 🐳 Ready-to-run **Docker** setup for easy deployment

---

## 🧩 Tech Stack

- **Python 3.11+**
- **Streamlit** — frontend framework  
- **Requests** — for fetching Microsoft IP data  
- **ipaddress / re / json** — for parsing and validation  
- **Docker / Docker Compose** — for containerized deployment

---

## 📦 Installation (Local)

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/azure-ip-extractor.git
   cd azure-ip-extractor
