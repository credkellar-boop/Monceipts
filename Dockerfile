# Use official Python image
FROM mcr.microsoft.com/playwright/python:v1.41.0-jammy

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers and dependencies
RUN playwright install chromium
RUN playwright install-deps

# Copy the rest of the application
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Start the application
CMD ["uvicorn", "app.backend.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
