 # Core Project Documentation

This document provides instructions and information about the `core` Django project.

## Project Overview

This is a simple Django project with a custom user authentication system. It includes user registration and login functionality.

## Setup and Installation

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone <repository-url>
    cd Django/core
    ```

2.  **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    This project doesn't have a `requirements.txt` file yet. Based on the project structure, you'll need at least Django.
    ```bash
    pip install Django
    ```
    It's good practice to create a `requirements.txt` file:
    ```bash
    pip freeze > requirements.txt
    ```

4.  **Create the database:**
    This project uses SQLite, which is a file-based database. The `migrate` command will create the `db.sqlite3` file and set up the necessary tables based on your models.
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser** (for accessing the Django admin):
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create an administrator account.

## Running the Development Server

To run the project locally, use the `runserver` command:
```bash
python manage.py runserver
```
The application will be available at `http://127.0.0.1:8000/`.

## Project Structure

The project consists of a single Django app:

-   `authentication`: This app handles user registration and login.

The `public` directory contains static and media files:
-   `public/static`: for CSS, JavaScript, and images.
-   `public/media`: for user-uploaded files.

## Important Commands

Here are some of the most common `manage.py` commands:

-   `python manage.py runserver`: Starts the development server.
-   `python manage.py migrate`: Applies database migrations. This is how you create and update your database schema.
-   `python manage.py makemigrations`: Creates new migration files based on changes to your models.
-   `python manage.py collectstatic`: Collects all static files from your apps into a single directory (`staticfiles` in this project) for production deployment. This is useful for managing production files.
-   `python manage.py createsuperuser`: Creates an admin user.
-   `python manage.py shell`: Opens a Python shell with the Django project environment loaded.

## Key Imports and Code Explanation

### `authentication/views.py`

This file contains the views for the `authentication` app.

-   `from django.shortcuts import render, redirect`:
    -   `render`: Renders a template with a given context and returns an `HttpResponse` object.
    -   `redirect`: Redirects the user to another URL.

-   `from django.contrib.auth import authenticate, login`:
    -   `authenticate`: Checks user credentials (username and password) and returns a user object if they are correct.
    -   `login`: Handles the session for a logged-in user.

-   `from django.contrib.auth.models import User`: This imports Django's built-in User model, which is used for storing user information.

### `core/settings.py`

This file contains the project's settings.

-   `INSTALLED_APPS`: A list of all Django applications that are activated in this project.
-   `DATABASES`: A dictionary containing the settings for all databases to be used with this project.
-   `STATIC_URL`, `STATIC_ROOT`, `STATICFILES_DIRS`: These settings are for configuring how Django handles static files (CSS, JavaScript, images).
    - `STATIC_URL`: The URL to use when referring to static files located in `STATIC_ROOT`.
    - `STATIC_ROOT`: The absolute path to the directory where `collectstatic` will collect static files for deployment.
    - `STATICFILES_DIRS`: A list of directories where Django will also look for static files.

## Static and Production Files

-   **Development**: In development (`DEBUG = True`), Django automatically serves static files from the directories listed in `STATICFILES_DIRS` and the `static` subdirectories of each app.
-   **Production**: In a production environment (`DEBUG = False`), you should use a dedicated web server (like Nginx or Apache) to serve static files. The `collectstatic` command gathers all the static files into the `STATIC_ROOT` directory (`staticfiles` in this project) so the web server can easily find them.
    ```bash
    python manage.py collectstatic
    ```
    This command will create a `staticfiles` directory in your project's root and copy all static files into it.

This `README.md` file should serve as a good starting point for your project's documentation.
