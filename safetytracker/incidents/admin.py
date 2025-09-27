from django.contrib import admin
from .models import IncidentReport

@admin.register(IncidentReport)
class IncidentReportAdmin(admin.ModelAdmin):
    """
    Customize the admin interface for IncidentReport.

    - display key columns in the list view: 'id', 'reporter', 'severity',
        'location', 'status', and 'date_reported'.
    
    - add sidebar filters for severity, status, and location.

    - provide search box for reporter username, description, and location.

    - adds a date-based nav bar for filtering by date_reported
    """

    list_display = ('id', 'reporter', 'severity', 'location', 'status', 'date_reported')
    list_filter = ('severity', 'status', 'location')
    search_fields = ('reporter_username', 'description', 'location')
    date_hierarchy = 'date_reported'