from django.shortcuts import render, get_object_or_404
from incidents.models import IncidentReport
from .models import SafetyMetric

# Create your views here.
def dashboard_home(request):
    # -date_reported will show most recent reports first
    incidents = IncidentReport.objects.all().order_by('-date_reported')
    context = {'incidents': incidents}

    return render(request, 'dashboard/dashboard_home.html', context)


def safety_metric_detail(request, pk):
    metric = get_object_or_404(SafetyMetric, pk=pk)

    return render(request, 'dashboard/safety_metric_detail.html', {'metric': metric})


def safety_metric_list(request):
    metrics = SafetyMetric.objects.all().order_by('-created_at')

    return render(request, 'dashboard/safety_metric_list.html', {'metrics': metrics})

