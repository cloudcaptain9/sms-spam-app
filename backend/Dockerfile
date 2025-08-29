# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements from backend directory
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend files
COPY backend/app.py ./
COPY backend/models/ ./models/
# COPY backend/.env ./  # Uncomment if needed

# Expose port
EXPOSE 8000

# Run the Flask app
CMD ["python", "app.py"]