# Task Manager REST API

A REST API built with Django and Django REST Framework. Users can register, log in with a token, and manage their own tasks.

## Features
- User registration and token authentication
- Full CRUD for tasks
- Each user can only see and edit their own tasks
- Automated tests

## Setup
```
pip install django djangorestframework
python manage.py migrate
python manage.py runserver
```

## Endpoints
| Method | URL | Description |
|--------|-----|-------------|
| POST | /api/register/ | Create a new user |
| POST | /api/login/ | Get an auth token |
| GET | /api/tasks/ | List your tasks |
| POST | /api/tasks/ | Create a task |
| PATCH | /api/tasks/{id}/ | Update a task |
| DELETE | /api/tasks/{id}/ | Delete a task |

Send the token in the header: `Authorization: Token <your_token>`

## Run tests
```
python manage.py test
```

## Tech Stack
Python, Django, Django REST Framework, SQLite