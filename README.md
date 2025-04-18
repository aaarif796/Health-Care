# Healthcare Management API

A comprehensive Django REST Framework-based backend system for managing healthcare data. This project allows secure registration, login, and full CRUD operations for patients and doctors with proper authentication. It supports patient-doctor mapping and uses PostgreSQL for efficient and scalable data storage.

---

## Summary

- Robust backend architecture using **Django**, **Django REST Framework**, and **PostgreSQL**
- Secured authentication via **JWT** using `djangorestframework-simplejwt`
- Fully functional **REST APIs** for managing patients, doctors, and mappings
- Developed with deep understanding of **DSA**, **LLMs**, **transformers**, and modern web backend frameworks including **Flask**
- Tested thoroughly using **Postman** with proper access token handling

---

## Features

- JWT-based user registration and login
- Create, retrieve, update, and delete Patients and Doctors
- Patient–Doctor relationship mapping
- Secured endpoints with authentication permissions
- Token Refresh functionality
- Clean project structure following best practices
- API tested using Postman with access/refresh tokens

---

## Tech Stack

- **Backend Framework:** Django, Django REST Framework
- **Authentication:** JWT (`djangorestframework-simplejwt`)
- **Database:** PostgreSQL
- **Testing:** Postman
- **Language:** Python
- **Others:** Flask (for microservice prototyping), DSA, LLMs, Transformers

---

## Project Structure Overview

```plaintext
Health-Care/
│
├── healthcare/
|   ├── controller
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── serializers.py
        ├── tests.py
        ├── urls.py
        ├── views.py
    ├── healthcare
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        ├── wsgi.py
|   ├── .env
|   ├── db.sqlite3
|   ├── manage.py
│
├── README.md
└── requirements.txt
```
---

## Installation

```bash
# Clone the repository
git clone https://github.com/aaarif796/Health-Care.git
cd Health-Care

# Create a virtual environment & activate it
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure PostgreSQL in settings.py
# Example:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'healthcare_db',
#         'USER': 'your_user',
#         'PASSWORD': 'your_password',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# Run migrations
python manage.py migrate

# Create a superuser (for admin access)
python manage.py createsuperuser

# Run the server
python manage.py runserver
```

---

## Authentication (JWT)

```bash
# Register a new user
POST /api/auth/register/

# Login to get access and refresh token
POST /api/auth/login/
# Body:
{
  "username": "your_username",
  "password": "your_password"
}

# Refresh token
POST /api/auth/token/refresh/
# Body:
{
  "refresh": "<your_refresh_token>"
}
```

**Include the JWT Access Token in Headers for secured routes:**

```http
Authorization: Bearer <your_access_token>
```

---

## Testing API Endpoints (Use Postman or any API client)

### Doctor Endpoints

```http
GET    /api/doctors/                 # List all doctors
POST   /api/doctors/                 # Add a new doctor
GET    /api/doctors/<id>/            # Get specific doctor by ID
```

### Patient Endpoints

```http
GET    /api/patients/                # List all patients
POST   /api/patients/                # Add a new patient
GET    /api/patients/<id>/           # Get specific patient by ID
```

### Mapping Endpoints (Patient-Doctor Relation)

```http
GET    /api/mappings/                # List or create patient-doctor mappings
POST   /api/mappings/                # Create a mapping
#Body:
{
  "patient":<patient_id>,
  "doctor":<doctor_id>
}
```

---

## Features

- Secure authentication with JWT
- Modular project structure with Django best practices
- Role-based access to patients and doctors
- PostgreSQL for scalable data management
- Tested using Postman (easy-to-use API testing)

---


---
