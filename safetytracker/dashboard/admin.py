from django.contrib import admin
from .models import SafetyMetric

@admin.register(SafetyMetric)
class SafetyMetricAdmin(admin.ModelAdmin):
    #displays these field names on the admin page
    list_display = ('created_at', 'total_incidents', 'high_severity_incidents')
    #add a nav bar at the top of the change list page
    date_hierarchy = 'created_at'