from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    We inherit all the standard Django user fields (username, password, email, is_staff, etc)
    including authentication

    Adds a 'role' field to distinguish between employees and managers.

    Class Fields:
        role: the role of the user, either 'EMPLOYEE', or 'MANAGER'
    """

    ROLE_CHOICES = [
        ('EMPLOYEE', 'employee'),
        ('MANAGER', 'manager'),
    ]

    role = models.CharField(max_length=25, choices=ROLE_CHOICES, default='EMPLOYEE')

    def __str__(self):
        return f'{self.username} ({self.role})'