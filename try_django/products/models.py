from django.db import models

# Create your models here.

class Product(models.Model):
    title       = models.CharField(max_length=255)
    description = models.TextField(blank= True , null=True)
    price       = models.DecimalField(decimal_places=2 , max_digits=1000000)
    summary     = models.TextField()
    featured    = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title 


