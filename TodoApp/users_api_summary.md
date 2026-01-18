# User and API Code Summary

This document summarizes the user-related and API code in the project.

## User Management (users app)

The `users` application handles user authentication and management through web-based views. It does not currently expose a REST API for user management.

Key components:

- **`users/views.py`**:
    - `MyLoginView`: A class-based view that handles user login. It uses the `login.html` template and redirects authenticated users to the main task list.
    - `RegisterView`: A class-based view for new user registration. It uses the `register.html` template and the `RegisterForm` form. Upon successful registration, the new user is logged in and redirected to the task list.

- **`users/urls.py`**:
    - Defines URL patterns for login, logout, registration, and password reset functionalities.

## Todo API (api app)

The `api` application provides a REST API for managing "To-do" items (`Task` model). Access to this API is restricted to authenticated users, and they can only view and manage their own tasks.

Key components:

- **`api/views.py`**:
    - `TodoList`: A `ListCreateAPIView` that allows authenticated users to list their existing tasks or create new ones.
    - `TodoDetail`: A `RetrieveUpdateDestroyAPIView` that allows authenticated users to view, update, or delete a specific task.

- **`api/urls.py`**:
    - `todos/`: Endpoint for the `TodoList` view.
    - `todos/<int:pk>/`: Endpoint for the `TodoDetail` view.

- **`api/permissions.py`**:
    - `IsOwnerOnly`: A custom permission class that ensures users can only access and modify their own `Task` objects.
