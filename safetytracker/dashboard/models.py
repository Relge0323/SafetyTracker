from django.db import models

# Create your models here.
class SafetyMetric(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    total_incidents = models.PositiveIntegerField()
    high_severity_incidents = models.PositiveIntegerField()

    def __str__(self):
        return f'Metrics as of {self.created_at}'