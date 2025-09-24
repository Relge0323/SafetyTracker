from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('metrics/', views.safety_metric_list, name='safety_metric_list'),
    path('metrics/<int:pk>/', views.safety_metric_detail, name='safety_metric_detail'),
]