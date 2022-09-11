from django.urls import path
from .views import companyDetails, dashboard

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('company/<int:pk>/', companyDetails, name="company_details"),
]