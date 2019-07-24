from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    # picture = models.ImageField(upload_to="app01/images",default="app01/images/1.png")