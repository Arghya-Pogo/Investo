from django.shortcuts import render

# Create your views here.
def onBoarding(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'Authentication/onboarding.html', context)