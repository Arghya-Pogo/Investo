from django import forms
from .models import Company

class CompanyCreateForm(forms.ModelForm):
    fb_link = forms.URLField(required=True)
    ig_link = forms.URLField(required=True)
    tw_link = forms.URLField(required=True)
    li_link = forms.URLField(required=True)
    
    class Meta:
        model = Company
        fields = [
            'company_name', 'company_email',
            'company_phone', 'company_logo', 'company_site',
            'company_description', 'company_history', 'company_funding',
            'company_aquisition', 'company_competition', 'company_founder_detail',
            'company_fundamental', 'company_industry', 'company_exname',
            'company_hq', 'company_mc', 'company_rev',
            'company_employes', 'fb_link', 'ig_link', 'tw_link',
            'li_link', 'finances', 'company_logo', 'establishment_date'
        ]
