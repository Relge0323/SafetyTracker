from django.shortcuts import render
from incidents.models import IncidentReport

# Create your views here.
def dashboard_home(request):
    # -date_reported will show most recent reports first
    incidents = IncidentReport.objects.all().order_by('-date_reported')
    context = {'incidents': incidents}

    return render(request, 'dashboard/dashboard_home.html', context)