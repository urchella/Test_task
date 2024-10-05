from django.db import models
from django.contrib.auth.models import User

class Cats(models.Model):
    name = models.CharField(max_length=40)
    color=models.CharField(max_length=20)
    age=models.IntegerField()
    description=models.TextField(blank=False)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    breed=models.ForeignKey('Breeds', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Breeds(models.Model):
    breed=models.CharField(max_length=40)

    def __str__(self):
        return self.breed
    

