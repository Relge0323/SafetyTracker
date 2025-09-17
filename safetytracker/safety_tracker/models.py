from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = [
        ('EMPLOYEE', 'employee'),
        ('MANAGER', 'manager'),
    ]

    role = models.CharField(max_length=25, choices=ROLE_CHOICES, default='EMPLOYEE')

    def __str__(self):
        return f'{self.username} ({self.role})'