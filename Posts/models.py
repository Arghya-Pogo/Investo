from django.db import models
from djrichtextfield.models import RichTextField
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Company(models.Model):
    """Model definition for Company."""

    founder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="company_founder")
    company_name = models.CharField(null=False, max_length=150)
    company_logo = models.ImageField(default='default_user__image.png', upload_to='profile_pics')
    company_email = models.EmailField(null=False, max_length=254)
    company_details = RichTextField()

    employes = models.IntegerField()
    interested_investors = models.ManyToManyField(User, null=True, blank=True)

    legal_info = models.FileField(null=True, blank=True, default=None, upload_to="legal_info")
    b_model = models.FileField(null=True, blank=True, default=None, upload_to="b_model")
    transaction_proof = models.FileField(null=True, blank=True, default=None, upload_to="transaction_proof")
    market_cap = models.FileField(null=True, blank=True, default=None, upload_to="market_cap")
    finances = models.FileField(null=True, blank=True, default=None, upload_to="finances")
    other_Details = models.FileField(null=True, blank=True, default=None, upload_to="other_Details")

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