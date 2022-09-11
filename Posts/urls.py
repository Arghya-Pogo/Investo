from django.urls import path
from .views import companyCreate, companyDetails, dashboard

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('company/<int:pk>/', companyDetails, name="company_details"),
    path('company/create/', companyCreate, name="company_create"),
]