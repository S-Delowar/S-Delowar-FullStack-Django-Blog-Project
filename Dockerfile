# # Pull a base image
# FROM python:3.11-bullseye

# # Set environemnt variables
# ENV PIP_DISABLE_PIP_VERSION_CHECK=1
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# # Set work directory
# WORKDIR /code

# # Install system dependencies
# RUN apt-get update && apt-get install -y gcc libpq-dev

# # Install project dependencies
# COPY ./requirements.txt .
# # RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt


# # Copy object files
# COPY . .

# # Expose application port
# EXPOSE 8000



# ==============================================================================================================






# Use official Python image
FROM python:3.11-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /code

# Install dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose application port
EXPOSE 8000

# Run Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "blog_project.wsgi:application"]
