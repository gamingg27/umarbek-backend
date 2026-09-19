from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("manager", "Manager"),
        ("teacher", "Teacher"),
        ("staff", "Staff"),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="staff")
    phone = models.CharField(max_length=30, blank=True)
