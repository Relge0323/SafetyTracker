from django.urls import path
from . import views

urlpatterns = [
    path('', views.incident_list, name='incident_list'),
    path('<int:pk>/', views.incident_detail, name='incident_detail'),
]
