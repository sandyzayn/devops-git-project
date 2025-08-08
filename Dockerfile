# Use official Python image
FROM python:3.11-slim

WORKDIR /app

COPY . .

# Install dependencies if requirements.txt exists
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

CMD ["python", "main.py"]
