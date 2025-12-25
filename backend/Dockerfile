# Dockerfile for Cloud Run deployment
FROM python:3.13-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend directory
COPY . .

# Set Python path so src is importable
ENV PYTHONPATH=/app

# Expose port (Cloud Run uses 8080)
EXPOSE 8080

# Set PORT environment variable for Cloud Run
ENV PORT=8080

# Run the API server
CMD ["python", "api_server.py"]

