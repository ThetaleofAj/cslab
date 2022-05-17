from django.db import models

# Create your models here.
class Data(models.Model):
   information = models.CharField(max_length=100)
   timeStamp = models.DateTimeField(auto_now_add=True,auto_now=False)

   def __str__(self):
      return self.information
      