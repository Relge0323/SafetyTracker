from django.contrib import admin
from .models import SafetyMetric

@admin.register(SafetyMetric)
class SafetyMetricAdmin(admin.ModelAdmin):
    """
    Customize the admin interface for SafetyMetric.

    - displays the 'created_at', 'total_incidents', and 'high_severity_incidents'
      columns in the list view

    - adds a date-based navigation bar at the top for easy filtering by creation date.
    """
    
    list_display = ('created_at', 'total_incidents', 'high_severity_incidents')
    date_hierarchy = 'created_at'