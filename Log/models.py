from datetime import datetime

from django.db import models

emotionlist = (("Very Happy", "Very Happy"),
               ("Happy", "Happy"),
               ("Content", "Content"),
               ("Dissatisfied", "Dissatisfied"),
               ("Extremely Dissatisfied", "Extremely Dissatisfied"))


# Create your models here.
class Logbook(models.Model):
    """"
    A model for logbook entries.
    """

    date = models.DateField(default=datetime.now)
    task = models.CharField(max_length=30, default=" ")
    description = models.TextField()
    emotion = models.CharField(max_length=30, choices=emotionlist, )
    hours_worked = models.DecimalField(max_digits=4, decimal_places=2)
