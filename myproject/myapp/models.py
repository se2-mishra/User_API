from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    mobile = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()

    def save(self, *args, **kwargs):
        # Add validation logic here before saving the user
        # For example, validate username, mobile, email, and password
        
        super(User, self).save(*args, **kwargs)
