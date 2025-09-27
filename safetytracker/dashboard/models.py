from django.db import models

class SafetyMetric(models.Model):
    """
    Stores a snapshot of metrics for safety incidents, used in the dashboard.

    Every record represents aggregated stats at a point in time.
    Managers will use these snapshots to monitor trends and safety performance
    """

    # using auto_now_add will make timestamps automatic
    created_at = models.DateTimeField(auto_now_add=True)
    total_incidents = models.PositiveIntegerField()
    high_severity_incidents = models.PositiveIntegerField()



    def __str__(self):
        return f'Metrics as of {self.created_at}'
    

    
    # show the most recent metrics first
    class Meta:
        ordering = ['-created_at']