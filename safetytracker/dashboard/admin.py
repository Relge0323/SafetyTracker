from django.contrib import admin
from .models import SafetyMetric

# Register your models here.
@admin.register(SafetyMetric)
class SafetyMetricAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'total_incidents', 'high_severity_incidents')
    date_hierarchy = 'created_at'