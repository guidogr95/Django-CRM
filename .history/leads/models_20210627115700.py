from django.db import models

class Lead(models.Model):
  first_name = models.CharField(max_length=40)
  last_name = models.CharField(max_length=40)
  age = models.IntegerField(default=0)
  phoned = models.BooleanField(default=False)
