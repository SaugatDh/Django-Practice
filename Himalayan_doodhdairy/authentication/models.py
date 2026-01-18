# from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings


class CustomUser(AbstractUser):
    username = None  # Remove username field
    email = models.EmailField("Email Address", unique=True)
    middle_name = models.CharField(max_length=50, default="", blank=True)
    
    phone_regex = RegexValidator(
        regex=r'^(?:\+?977-?)?(97|98)\d{8}$',
        message="Invalid Nepali phone number."
    )
    phone = models.CharField(validators=[phone_regex], max_length=15, unique=True)

    is_staff_user = models.BooleanField(default=False)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [] # No username or phone required for createsuperuser

    def __str__(self):
        # Careful: You originally referenced self.username here, 
        # but since that is None, let's use email instead.
        return f"{self.first_name} {self.last_name} ({self.email})"
    
