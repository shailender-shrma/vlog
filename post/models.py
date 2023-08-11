from django.db import models
from user.models import Signup
# Create your models here.

class Post(models.Model):
    
    author = models.ManyToManyField(Signup,max_length=255)
    description = models.CharField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.author