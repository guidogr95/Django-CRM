from django.db import models

class Lead(models.Model):
  first_name = models.CharField(max_length=40)
  last_name = models.CharField(max_length=40)
  age = models.IntegerField(default=0)
  # foreign key ==> every agen can have many leads
  agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
  
class Agent(models.Model):
  first_name = models.CharField(max_length=40)
  last_name = models.CharField(max_length=40)

  
  