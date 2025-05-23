from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
import datetime
current=datetime.datetime.now().year
# Create your models here.
class User (AbstractUser):
    

    department = models.CharField(max_length=100,default="MCA")
    year = models.IntegerField(default=current)
    is_coordinator = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        # Ensure the password is hashed when saving manually
        if self.pk is None or not self.password.startswith("pbkdf2_sha256$"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    

 