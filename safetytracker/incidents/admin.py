from django.contrib import admin
from .models import IncidentReport

# Register your models here.
@admin.register(IncidentReport)
class IncidentReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'reporter', 'severity', 'location', 'status', 'date_reported')

    #add a sidebar to filter displayed records by field value
    list_filter = ('severity', 'status', 'location')

    #adds a search box for the strings in the tuple
    search_fields = ('reporter_username', 'description', 'location')

    #add a nav bar at the top of the change list page
    date_hierarchy = 'date_reported'