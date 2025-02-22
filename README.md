# Django Blog Project

A full-stack blog platform built with Django, designed for seamless blog creation, reading, commenting, and liking. This project is containerized using **Docker**, integrated with **Nginx**, **Gunicorn**, and **PostgreSQL** and tested with CI/CD pipelines using GitHub Actions for deploying on AWS cloud.

## CI/CD Pipeline:
- Automated build and deployment using GitHub Actions.
- Docker image built and pushed to AWS ECR (Elastic Container Registry).
- Deployment to AWS EC2 instance using docker-compose.
- Environment variables and secrets managed securely via GitHub Repository Secrets.


## Features
The project leverages modern tools such as **Django Allauth** for user authentication, **Crispy Forms** for styled forms, **SendGrid** for email services.

### User Authentication:
- User registration, login, and password management.
- Social account login via `django-allauth[socialaccount]`.

### Blog Management:
- Create, edit, delete, and view blogs.
- Rich text handling with image support (via **Pillow**).

### Comments and Likes:
- Authenticated users can comment on and like blog posts.

### Responsive Forms:
- Styled forms using **Crispy Forms** and **Bootstrap 5**.

### Email Integration:
- Password verifications and resets using **SendGrid**.

### Debugging Tools:
- Integrated **Django Debug Toolbar** for easier development debugging.

### Production-Ready Setup:
- **Nginx** is used for reverse proxy configuration and serving static files.
- WSGI server using **Gunicorn**.
- **PostgreSQL** as the production database.

