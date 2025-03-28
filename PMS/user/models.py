from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

# Create your models here.
class User (AbstractUser):
    DEPARTMENT_CHOICES = [
        ("MCA", "MCA"),
        ("CSE", "CSE"),
        ("IT", "IT"),
        ("ECE", "ECE"),
    ] 
    YEAR_CHOICES = [(year, str(year)) for year in range(2020, 2031)]  # 2020 to 2030

    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES, blank=True, null=True)
    year = models.IntegerField(choices=YEAR_CHOICES, blank=True, null=True)
    is_coordinator = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        # Ensure the password is hashed when saving manually
        if self.pk is None or not self.password.startswith("pbkdf2_sha256$"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    

 