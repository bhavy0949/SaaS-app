# Use official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
# Gunicorn is needed for running Django in production
RUN pip install gunicorn

# Copy project files
COPY . /app/

# Expose port
EXPOSE 8000

# Start server using gunicorn instead of python manage.py runserver
# --chdir points to the src directory where manage.py and SaaS live
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--chdir", "src", "SaaS.wsgi:application"]
