from django.db import models
import uuid


# Create your models here.
class ContactPerson(models.Model):

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    topic = models.TextField(max_length=500)