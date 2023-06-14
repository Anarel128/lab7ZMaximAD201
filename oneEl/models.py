from django.db import models

class Own(models.Model):
    name = models.CharField(max_length=120)
    package = models.IntegerField()
    modelgaika  = models.IntegerField(default=0)
    telef = models.IntegerField()
    addres = models.CharField(max_length=1000)



