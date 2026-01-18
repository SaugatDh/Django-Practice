# Himalayan DoodhDairy - Documentation & Tutorial

This document provides a comprehensive overview, setup guide, and step-by-step tutorial for the Himalayan DoodhDairy Django project.

> **Original Prompt:** "make me documentation for the himalayan doodhdairy . Show all database design, code important ones, guide like tutorial. step by step approach, from authentication app design to orders and so on."

---

## 1. Project Overview

Himalayan DoodhDairy is a web application designed to manage milk orders. It has two primary types of users: **Customers**, who can sign up, log in, and place orders for milk, and **Staff Members**, who can view all orders and manage deliveries.

The project is built using the Django framework and is divided into two main applications:
- **`authentication`**: Handles user creation, login, logout, and management. It uses a custom user model to cater to the specific needs of the application.
- **`orders`**: Manages the creation, viewing, and assignment of milk orders.

---

## 2. Setup and Installation

Follow these steps to get the project running on your local machine.

**Prerequisites:**
- Python 3.x
- `pip` (Python package installer)

**Steps:**

1.  **Clone the Repository:**
    ```bash
    git clone <your-repository-url>
    cd Himalayan_doodhdairy
    ```

2.  **Install Dependencies:**
    It's recommended to use a virtual environment.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install Django
    # (Add other dependencies from requirements.txt if available)
    ```

3.  **Apply Database Migrations:**
    This command creates the necessary database tables based on your models.
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4.  **Create a Superuser:**
    A superuser account is needed to access the Django Admin interface.
    ```bash
    python manage.py createsuperuser
    ```
    You will be prompted to enter an email, password, and other details.

5.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000`.

---

## 3. Database Design

The database consists of three main tables spread across two apps.

### `authentication` App

#### **`CustomUser` Model**
This model extends Django's `AbstractUser` to create a tailored user system. The `email` field is used as the unique identifier for login instead of a username.

| Field Name | Type | Description |
| :--- | :--- | :--- |
| `id` | AutoField | Primary Key. |
| `password` | CharField | Hashed user password. |
| `last_login` | DateTimeField | Records the last login timestamp. |
| `email` | EmailField | **UNIQUE**. Used as the `USERNAME_FIELD` for authentication. |
| `first_name`| CharField | User's first name. |
| `middle_name`| CharField | User's middle name (optional). |
| `last_name` | CharField | User's last name. |
| `phone` | CharField | **UNIQUE**. Stores Nepali phone numbers, with validation. |
| `is_staff` | BooleanField | Designates if the user can access the admin site or has staff privileges. |
| `is_superuser`| BooleanField | Designates that this user has all permissions without explicit assignment. |
| `is_active` | BooleanField | Designates whether this user account should be considered active. |
| `date_joined`| DateTimeField| The date and time the account was created. |

### `orders` App

#### **`MilkOrder` Model**
This model stores information about a specific milk order placed by a customer.

| Field Name | Type | Description |
| :--- | :--- | :--- |
| `id` | AutoField | Primary Key. |
| `user` | ForeignKey | A many-to-one relationship to `CustomUser`. The customer who placed the order. |
| `milk_type` | CharField | The type of milk, chosen from 'cow' or 'buffalo'. |
| `quantity` | DecimalField | The amount of milk ordered, in liters. |
| `order_at` | DateTimeField | Automatically records the timestamp when the order was created. |

#### **`OrderAssignment` Model**
This model links a `MilkOrder` to a staff member for delivery and tracks its status.

| Field Name | Type | Description |
| :--- | :--- | :--- |
| `id` | AutoField | Primary Key. |
| `order` | OneToOneField| A one-to-one relationship to `MilkOrder`. Each order can have only one assignment. |
| `staff_member`| ForeignKey | A many-to-one relationship to `CustomUser`, limited to users where `is_staff=True`. |
| `status` | CharField | The current status of the delivery ('pending', 'on_the_way', 'delivered'). |
| `delivery_notes`| TextField | Optional notes from the delivery person. |

---

## 4. Application Logic: A Step-by-Step Guide

### Part I: The `authentication` App

This app handles everything related to user accounts.

#### 1. The Custom User Model (`authentication/models.py`)
We use a custom user model to enforce unique email and phone numbers and to use email for login.

```python
# authentication/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    username = None  # Remove username field
    email = models.EmailField("Email Address", unique=True)
    middle_name = models.CharField(max_length=50, default="", blank=True)
    
    phone_regex = RegexValidator(
        regex=r'^(?:\+?977-?)?(97|98)\d{8}$',
        message="Invalid Nepali phone number."
    )
    phone = models.CharField(validators=[phone_regex], max_length=15, unique=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
```

#### 2. Views for Signup, Login, and Logout (`authentication/views.py`)

- **`signup_view`**: Renders the registration form and handles the creation of a new `CustomUser`. It includes basic validation for matching passwords and existing emails.
- **`login_view`**: Authenticates users against the `CustomUser` model using their email and password. On successful login, it redirects them to the `home` page.
- **`logout_view`**: Logs the user out and redirects them to the login page.

```python
# authentication/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import CustomUser

def signup_view(request):
    if request.method == "POST":
        # ... (logic for creating a user)
        user = CustomUser(email=email, phone=phone)
        user.set_password(password) 
        user.save()
        messages.success(request, "Account created successfully")
        return redirect("login")
    return render(request, "signup.html")

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.email}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password.")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login') 
```

#### 3. URL Routing (`authentication/urls.py` and `Himalayan_doodhdairy/urls.py`)
The app's URLs are defined and then included in the main project's URL configuration, prefixed with `auth/`.

```python
# authentication/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
```

```python
# Himalayan_doodhdairy/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')), # <-- Authentication URLs
    path('staff/', include('orders.urls')),
]
```

This means the signup page is at `/auth/signup/` and the login page is at `/auth/login/`.

### Part II: The `orders` App

This app is the core of the dairy management system.

#### 1. Order Models (`orders/models.py`)
The models define the structure for orders and their assignments, as detailed in the Database Design section.

```python
# orders/models.py
from django.db import models
from django.conf import settings

class MilkOrder(models.Model):
    # ... (fields as defined above) ...

class OrderAssignment(models.Model):
    # ... (fields as defined above) ...
```

#### 2. The Home View (`orders/views.py`)
This is the central view of the application, protected by the `@login_required` decorator. It serves two different purposes based on the user type:

- **For Customers (`is_staff=False`):**
  - It displays a form to place a new milk order (`POST`).
  - It lists all past orders placed by that specific customer (`GET`).

- **For Staff Members (`is_staff=True`):**
  - It displays a list of **all** milk orders from all customers, allowing them to monitor the system.

```python
# orders/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import MilkOrder

@login_required
def home_view(request):
    # --- For Customers placing an order ---
    if request.method == "POST" and not request.user.is_staff:
        # ... (logic to create MilkOrder) ...
        messages.success(request, "Order placed successfully!")
        return redirect('home')

    # --- Displaying data based on user type ---
    context = {}
    if request.user.is_staff:
        # Staff sees all orders
        context['orders'] = MilkOrder.objects.all().order_by('-order_at')
    else:
        # Customer sees only their own orders
        context['my_orders'] = MilkOrder.objects.filter(user=request.user).order_by('-order_at')

    return render(request, 'home.html', context)
```

#### 3. URL Routing (`orders/urls.py`)
The `home_view` is mapped to the `home/` URL. This app's URLs are prefixed with `staff/` in the main project, making the final URL `/staff/home/`.

```python
# orders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
]
```
*Note: The main `urls.py` includes this as `path('staff/', include('orders.urls'))`. The naming might seem confusing; a better prefix might be `dashboard/` or `orders/`.*

---

## 5. Django Admin Interface

The Django Admin provides a powerful, ready-to-use interface for managing data. The models from both apps have been registered to be manageable through the admin panel.

#### `authentication/admin.py`
This file customizes how the `CustomUser` model is displayed in the admin. It defines list display fields, search fields, filters, and the layout of the user creation/editing forms.

```python
# authentication/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "first_name", "last_name", "phone", "is_staff")
    # ... other customizations
```

#### `orders/admin.py`
This registers the `MilkOrder` and `OrderAssignment` models, making it easy for a superuser to view, create, edit, and delete order records directly.

```python
# orders/admin.py
from django.contrib import admin
from .models import MilkOrder, OrderAssignment

@admin.register(MilkOrder)
class MilkOrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'milk_type', 'quantity', 'order_at')
    list_filter = ('milk_type', 'order_at')

@admin.register(OrderAssignment)
class OrderAssignmentAdmin(admin.ModelAdmin):
    list_display = ('order', 'staff_member', 'status')
    list_filter = ('status', 'staff_member')
```

To access the admin interface, navigate to `/admin/` and log in with the superuser account created during setup.
