# Use lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Expose port
EXPOSE 5000

# Run using gunicorn
CMD ["gunicorn", "--chdir", "src/main/python", "app:app", "--bind", "0.0.0.0:5000"]
