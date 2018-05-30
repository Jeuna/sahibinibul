from django.db import models
from django.conf import settings
import datetime
YEAR_CHOICES = []
for r in range(1900, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

class car (models.Model):
    renk = models.CharField(max_length=20,null=True,blank=True)
    model = models.CharField(max_length=50,null=True,blank=True)
    model_yili = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    plaka = models.CharField(max_length=10)
    sahip = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    tehlikede = models.IntegerField(default=0)

    def __str__(self):
        return self.plaka


