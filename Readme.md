# Classroom Management System

This is a Django-based web application for managing classroom resources, schedules, and maintenance records.

## Features

- Manage classroom resources
- Schedule resources
- Record maintenance activities

## Prerequisites

- Python 3.10 or higher
- MySQL

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/classroom-management.git
cd classroom-management
```
### 2. Create and Activate a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### 3. Install Dependencies
```sh
pip install -r requirements.txt
```
### 4. Apply Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```
### 5. Collect Static Files
```sh
python manage.py collectstatic
```
### 6. Create a Superuser
```sh
python manage.py createsuperuser
```
### 7. Run the Development Server
```sh
python manage.py runserver
```
### 8. Access the Application
Open your web browser and go to http://127.0.0.1:8000/ to access the application.

## Project Structure
classroom-management/
├── classroom/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
├── resources/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── images/
│   │   ├── logo.jpg
│   │   └── Smart_Classroom.jpg
│   └── ...
├── templates/
│   └── index.html
├── manage.py
└── requirements.txt