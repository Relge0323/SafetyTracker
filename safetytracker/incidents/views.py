from django.shortcuts import render, get_object_or_404
from .models import IncidentReport

def incident_list(request):
    """
    Display a list of all reported incidents, ordered by most recent
    
    Args:
        request: the current HTTP request object
    
    Returns:
        HttpResponse: renders 'incidents/incident_list.html'
        with all incidents in context
    """

    incidents = IncidentReport.objects.all().order_by('-date_reported')
    return render(request, 'incidents/incident_list.html', {'incidents': incidents})

def incident_detail(request, pk):
    """
    Display detailed info about a specific incident.

    Args:
        request: the current HTTP request object
        pk (int): the primary key of the IncidentReport to display

    Returns:
        HttpResponse: renders 'incidents/incident/detail.html'
        with the selected incident in context
    """

    incident = get_object_or_404(IncidentReport, pk=pk)
    return render(request, 'incidents/incident_detail.html', {'incident': incident})
