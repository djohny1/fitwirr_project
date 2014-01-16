from django.db import models

from django import forms


class Contact(models.Model):
    full_name = models.CharField(max_length=300, null=True, blank=True)
    email = models.EmailField()
    message = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self,):
        return "Message from: " + str(self.email)



