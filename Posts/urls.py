from django.urls import path
from .views import companyCreate, companyDetails, dashboard, searchCompany

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('company/search/', searchCompany, name="company_search"),
    path('company/<int:pk>/', companyDetails, name="company_details"),
    path('company/create/', companyCreate, name="company_create"),
]