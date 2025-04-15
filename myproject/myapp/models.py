from django.db import models

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100, default='Unnamed Feature')
    details = models.CharField(max_length=500, default='No details provided')

    # def __str__(self):
    #     return self.name