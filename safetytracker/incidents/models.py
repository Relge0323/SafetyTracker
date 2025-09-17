from django.db import models
from django.conf import settings

# Create your models here.
class IncidentReport(models.Model):
    SEVERITY_CHOICES = [
        ('LOW', 'low'),
        ('MEDIUM', 'medium'),
        ('HIGH', 'high'),
        ('CRITICAL', 'critical'),
    ]

    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reports')

    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    location = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='incident_photos/', blank=True, null=True)
    date_reported = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('OPEN', 'open'), ('IN_PROGRESS', 'in_progress'), ('CLOSED', 'closed')], default='OPEN')

    def __str__(self):
        return f'{self.severity} at {self.location} by {self.reporter}'