from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User)
    email = models.EmailField( null=True, blank=True)
    about = models.TextField(max_length=250, null=True, blank=True)
    weight = models.CharField(max_length=200, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True)
    goal = models.CharField(max_length=50, null=True, blank=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    
    def __unicode__(self,):
        return self.user.username

class UserPicture(models.Model):
    user = models.ForeignKey(User)
    image = models.ImageField(upload_to='profiles/')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=True)
    
    
    def __unicode__(self,):
        return str(self.image)
    
    
