from django.contrib import admin
from .models import Company

# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    '''Admin View for Company'''

    list_display = ('company_name', 'company_email', 'establishment_date', 'company_employes')
    list_filter = ('date_posted',)
    search_fields = ('company_name',)
    ordering = ('-date_posted',)