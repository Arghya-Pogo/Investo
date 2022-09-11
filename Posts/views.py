from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Company

# Create your views here.
@login_required
def dashboard(request):
    companies = Company.objects.all()

    context = {
        'companies': companies
    }

    return render(request, 'Posts/dashboard.html', context)


@login_required
def companyDetails(request, pk):
    company = get_object_or_404(Company, pk=pk)
    context = {
        'company': company
    }

    return render(request, 'Posts/company_details.html', context)