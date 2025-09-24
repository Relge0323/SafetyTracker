from django.shortcuts import render, get_object_or_404
from .models import IncidentReport

def incident_list(request):
    incidents = IncidentReport.objects.all().order_by('-date_reported')
    return render(request, 'incidents/incident_list.html', {'incidents': incidents})

def incident_detail(request, pk):
    incident = get_object_or_404(IncidentReport, pk=pk)
    return render(request, 'incidents/incident_detail.html', {'incident': incident})
