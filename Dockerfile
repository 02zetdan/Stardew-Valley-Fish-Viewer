FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Expose Flask port
EXPOSE 5000

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application files
COPY . .
WORKDIR /app/src/app
# Set environment variables (optional, better to do this in Kubernetes)
ENV PYTHONPATH=/app/src \
    FLASK_APP=app.py \
    FLASK_ENV=development \
    FLASK_DEBUG=1

# Start Flask
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
