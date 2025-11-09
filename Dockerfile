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

# Expose Streamlit default port
EXPOSE 8501

# Run Streamlit with production-friendly flags
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
