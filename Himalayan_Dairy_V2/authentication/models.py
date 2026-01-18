from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        # We remove 'username' from here because we are using email
        return self.create_user(email, password, **extra_fields)
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
    objects = CustomUserManager()
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
    
