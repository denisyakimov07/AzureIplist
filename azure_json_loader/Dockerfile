# Use lightweight Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency file if you have one, else create inline
COPY requirements.txt ./requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all app files
COPY . .

# Run Streamlit with production-friendly flags
CMD ["python", "-u", "azure_json_loader.py"]
