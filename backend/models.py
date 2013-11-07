from django.db import models

class AWSAccount(models.Model):
    name = models.CharField(max_length=64)
    access_key = models.CharField(max_length=64)
    secret_access_key = models.CharField(max_length=64)
    
    # Pretty print for this object
    def __str__(self):
        return 'Name:' , self.name
