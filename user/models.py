from django.db import models


# Create your models here.

class Signup(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254,unique=True)

    def __str__(self):
        return self.name
    
    
