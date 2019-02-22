from django.db import models

class WorkData(models.Model):
    date = models.DateTimeField()
    StartTime = models.DateTimeField()
    EndTime = models.DateTimeField()
    MorningOffFlg = models.BooleanField()
    AfternoonOffFlg = models.BooleanField()

            
            