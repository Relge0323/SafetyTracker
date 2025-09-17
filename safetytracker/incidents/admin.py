from django.contrib import admin
from .models import IncidentReport

# Register your models here.
@admin.register(IncidentReport)
class IncidentReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'reporter', 'severity', 'location', 'status', 'date_reported')
    list_filter = ('severity', 'status', 'location')
    search_fields = ('reporter_username', 'description', 'location')
    date_hierarchy = 'date_reported'