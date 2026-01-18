# TodoApp

This is a Django project for a Todo application with a REST API.

## Features

-   User registration and login
-   Create, read, update, and delete tasks
-   REST API with token-based authentication

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd TodoApp
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

4.  **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## API Usage

The API is protected by token-based authentication. To access the API, you need to obtain a JWT token.

### 1. Obtain a JWT Token

Send a POST request to `/api/v1/token/` with your username and password to obtain a token:

```bash
curl -X POST -H "Content-Type: application/json" -d '{
    "username": "your-username",
    "password": "your-password"
}' http://127.0.0.1:8000/api/v1/token/
```

The response will contain an `access` token and a `refresh` token:

```json
{
    "refresh": "...",
    "access": "..."
}
```

### 2. Access Protected Endpoints

To access protected endpoints, include the `access` token in the `Authorization` header as a Bearer token:

```bash
curl -X GET -H "Authorization: Bearer <access-token>" http://127.0.0.1:8000/api/v1/todos/
```

### 3. Refresh the Token

The `access` token has a short lifetime. When it expires, you can obtain a new one by sending a POST request to `/api/v1/token/refresh/` with your `refresh` token:

```bash
curl -X POST -H "Content-Type: application/json" -d '{
    "refresh": "<refresh-token>"
}' http://12v1/token/refresh/
```
The project also needs a requirements.txt file, which is missing. I will create one now.
```bash
pip freeze > requirements.txt
```
I will add the necessary dependencies to the file.
Django==4.2.13
djangorestframework==3.15.1
djangorestframework-simplejwt==5.3.1

I will now create the file.
