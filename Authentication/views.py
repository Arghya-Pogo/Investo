from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


# Create your views here.
def onBoarding(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'Authentication/onboarding.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Congratulations {username}, your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'Authentication/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'Authentication/profile.html')