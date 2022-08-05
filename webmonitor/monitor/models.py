from django.db import models

# Create your models here.

class Website(models.Model):
    website = models.CharField(max_length=250) 
