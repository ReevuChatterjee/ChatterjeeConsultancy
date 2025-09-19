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
    type=models.CharField(choices=PROJECT_TYPES)
    budget=models.CharField()
    describe=models.TextField()

    

# Create your models here.
