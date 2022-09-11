from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Company(models.Model):
    """Model definition for Company."""

    founder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="company_founder")
    company_name = models.CharField(null=False, max_length=150, default=None)
    company_logo = models.ImageField(default='default_user__image.png', upload_to='profile_pics')

    company_email = models.EmailField(null=False, max_length=254, default=None)
    company_phone = models.CharField(max_length=13, default=None)
    company_site = models.URLField(null=False, blank=False, default=None)


    company_description = models.TextField(max_length=1000, default=None)
    company_history = models.TextField(max_length=1000, default=None)
    company_funding = models.TextField(max_length=1000, default=None)
    company_aquisition = models.TextField(max_length=1000, default=None)
    company_competition = models.TextField(max_length=1000, default=None)
    company_founder_detail = models.TextField(max_length=1000, default=None)
    company_fundamental = models.TextField(max_length=1000, default=None)


    company_industry = models.CharField(max_length=150, default=None)
    company_exname = models.CharField(max_length=150, default=None)
    company_hq = models.CharField(max_length=150, default=None)
    company_mc = models.CharField(max_length=10, default=None)
    company_rev = models.CharField(max_length=10, default=None)

    company_employes = models.IntegerField()
    company_interested_investors = models.ManyToManyField(User, null=True, blank=True)

    fb_link = models.URLField(blank=True, default=None, null=False)
    ig_link = models.URLField(blank=True, default=None, null=False)
    tw_link = models.URLField(blank=True, default=None, null=False)
    li_link = models.URLField(blank=True, default=None, null=False)
    finances = models.FileField(null=True, blank=True, default=None, upload_to="finances")

    establishment_date = models.DateField()
    date_posted = models.DateTimeField(default=timezone.now)


    class Meta:
        """Meta definition for Company."""

        verbose_name = 'Company'
        verbose_name_plural = 'Companys'
        ordering = ['-date_posted']

    def __str__(self):
        """Unicode representation of Company."""
        return self.company_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.company_logo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)