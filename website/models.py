from django.db import models

class custRequest(models.Model):
    fullName=models.CharField(max_length=50)
    email=models.EmailField()
    PROJECT_TYPES = [
        ('residential', 'Residential'),
        ('commercial', 'Commercial'),
        ('interior', 'Interior'),
        ('urban', 'Urban / Landscape'),
    ]
    type=models.CharField(choices=PROJECT_TYPES,max_length=50)
    budget=models.CharField(max_length=50)
    describe=models.TextField()

    

# Create your models here.
