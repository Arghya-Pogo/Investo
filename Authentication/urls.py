from django.urls import path
from .views import onBoarding, profile, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', onBoarding, name="onboarding"),
    path('login/', auth_views.LoginView.as_view(template_name='Authentication/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Authentication/onboarding.html'), name='logout'),
    path('register/', register, name='register'),
    path('app/profile/', profile, name='profile')
]