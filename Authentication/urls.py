from django.urls import path
from .views import onBoarding

urlpatterns = [
    path('', onBoarding, name="onboarding"),
]