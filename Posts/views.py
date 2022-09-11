from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Company
from .forms import CompanyCreateForm

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


@login_required
def companyCreate(request):
    if request.method == 'POST':
        form = CompanyCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CompanyCreateForm()

    context = {
        'form': form
    }
    
    return render(request, 'Posts/company_create.html', context)