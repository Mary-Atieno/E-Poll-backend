from django.db import models
from accounts.models import * 
from cloudinary.models import CloudinaryField


# Create your models here.
class Voter(models.Model):
    admin = models.ManyToManyField(CustomUser)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,  unique=True)
    phone = models.CharField(max_length=11, unique=True)  
    verified = models.BooleanField(default=False)
    voted = models.BooleanField(default=False) 

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=50, unique=True)
    max_vote = models.IntegerField()
    priority = models.IntegerField()

    def __str__(self):
        return self.name


class Candidate(models.Model):
    fullname = models.CharField(max_length=50)
    image = CloudinaryField('image',blank=True)
    bio = models.TextField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname

class Votes(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)