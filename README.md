# Django Blog Project

A full-stack blog platform built with Django, designed for seamless blog creation, reading, commenting, and liking. This project is containerized using **Docker** and is deployment-ready with **Nginx**, **Gunicorn**, and **PostgreSQL**.

The project leverages modern tools such as **Django Allauth** for user authentication, **Crispy Forms** for styled forms, **SendGrid** for email services, and **Whitenoise** for efficient static file serving.

---

## Features

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
- Email notifications and password resets using **SendGrid**.

### Debugging Tools:
- Integrated **Django Debug Toolbar** for easier development debugging.

### Production-Ready Setup:
- Static and media file management with **Whitenoise**.
- Reverse proxy configuration using **Nginx**.
- WSGI server using **Gunicorn**.
- **PostgreSQL** as the production database.

---
