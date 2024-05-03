from django.db import models
import uuid

# Create your models here.
class ContactPerson(models.Model):

   name = models.CharField(max_length= 255)
   phone = models.CharField(max_length= 11)
   email = models.EmailField()
   topic = models.TextField(max_length= 500)

#   def __init__(self, name, phone, email, topic):
#      self.name = name
#      self.phone = phone
#      self.email = email
#      self.topic = topic
#
#   def __verifyperson(self):
#      name = models.CharField(max_length= 255, blank=True, null=True)
#      phone = models.CharField(max_length= 11, blank=True, null=True)
#      email = models.EmailField(blank=True, null=True)
#      topic = models.CharField(max_length= 500, blank=True, null=True)
#      
#
#   def __str__(self):
#       return self.name   