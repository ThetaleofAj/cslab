from django.db import models

# Create your models here.
class Data(models.Model):
   temperature = models.CharField(max_length=5)
   humidity = models.CharField(max_length=5)
   timeStamp = models.DateTimeField(auto_now_add=True,auto_now=False)

   def __str__(self):
      return self.temperature
      