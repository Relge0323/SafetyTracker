from django.shortcuts import render, get_object_or_404
from incidents.models import IncidentReport
from .models import SafetyMetric
from django.db.models import Q


def dashboard_home(request):
    """
    Main dashboard view showing recent incidents and current summary metrics.
    Managers can use this view to monitor safety issues in real time.

    Args:
        request: The current HTTP request object.
    
    Returns:
        HttpResponse: Renders'dashboard/dashboard_home.html' with incidents
        and summary metrics in context.
    """

    # -date_reported will show most recent reports first
    incidents = IncidentReport.objects.all().order_by('-date_reported')


    # calculate quick summary metrics
    total_incidents = incidents.count()
    high_severity_incidents = incidents.filter(Q(severity='HIGH') | Q(severity='CRITICAL')).count()
    open_incidents = incidents.filter(status='OPEN').count()

    context = {'incidents': incidents, 
               'total_incidents': total_incidents, 
               'high_severity_incidents': high_severity_incidents, 
               'open_incidents': open_incidents}

    return render(request, 'dashboard/dashboard_home.html', context)


def safety_metric_detail(request, pk):
    """
    Display detailed information about a specific SafetyMetric snapshot.
    Managers can use this view to analyze trends or review past data.

    Args:
        request: The current HTTP request object.
        pk (int): The primary key of the SafetyMetric to display

    Returns:
        HttpResponse: Renders 'dashboard/safety_metric_detail.html'
        with the selected metric in context.
    """

    metric = get_object_or_404(SafetyMetric, pk=pk)

    return render(request, 'dashboard/safety_metric_detail.html', {'metric': metric})


def safety_metric_list(request):
    """
    Display a list of historical SafetyMetric snapshots for possible trend analysis

    Args:
        request: The current HTTP request object
    
    Returns:
        HttpResponse: Renders 'dashboard/safety_metric_list.html' with all
        SafetyMetric objects in context, ordered by creation date descending.
    """

    metrics = SafetyMetric.objects.all().order_by('-created_at')

    return render(request, 'dashboard/safety_metric_list.html', {'metrics': metrics})

