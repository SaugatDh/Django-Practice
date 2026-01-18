# Learn Django - Official Tutorial Project

This document provides instructions and information about the `learn_django_official_docs` project. This project is the official Django tutorial application, a basic poll application.

## Project Overview

This project is a simple poll application that lets users view and vote on questions. It is the project created by following the official Django documentation tutorial, and it's a great way to learn the basics of the framework.

## Setup and Installation

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone <repository-url>
    cd Django/learn_django_official_docs
    ```

2.  **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    The `requirements.txt` file in this project lists Django as a dependency.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create the database:**
    This project uses SQLite. The `migrate` command will create the `db.sqlite3` file and set up the necessary tables for the `Question` and `Choice` models.
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
The application will be available at `http://127.0.0.1:8000/polls/`.

## The `polls` App

The `polls` app is the core of this project.

### `polls/models.py`

This file defines the data models for the application.

-   **`Question` model**: Represents a poll question.
    -   `question_text` (CharField)
    -   `pub_date` (DateTimeField)

-   **`Choice` model**: Represents a choice for a question.
    -   `question` (ForeignKey to `Question`)
    -   `choice_text` (CharField)
    -   `votes` (IntegerField)

### `polls/views.py`

This file contains the logic for displaying the polls and handling user input. It uses Django's generic class-based views.

-   **`IndexView` (ListView)**: Displays a list of the latest questions.
-   **`DetailView` (DetailView)**: Displays the details of a specific question, including its choices.
-   **`ResultsView` (DetailView)**: Displays the results of a poll.
-   **`votes(request, question_id)`**: Handles the voting process for a choice.

### Key Imports

-   `from django.views import generic`: Imports Django's generic class-based views, which provide a convenient way to handle common web development tasks, like displaying a list of objects or the details of a single object.
-   `from django.shortcuts import get_object_or_404, render`:
    -   `get_object_or_404`: A shortcut to get a Django object, raising a 404 error if the object is not found.
    -   `render`: A shortcut to render a template with a context.
-   `from django.urls import reverse`: Used to generate URLs for a given view. This helps to avoid hardcoding URLs in templates and views.

## Common `manage.py` Commands

-   `python manage.py runserver`: Starts the development server.
-   `python manage.py migrate`: Applies database migrations.
-   `python manage.py makemigrations polls`: Creates new migration files for the `polls` app if you change its models.
-   `python manage.py test polls`: Runs the tests for the `polls` app.
-   `python manage.py createsuperuser`: Creates an admin user.
-   `python manage.py shell`: Opens an interactive Python shell with the project's environment loaded.

This README should help you understand and work with this Django tutorial project.