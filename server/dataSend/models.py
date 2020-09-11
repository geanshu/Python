from django.db import models

class people_count(models.Model):
    testid = models.IntegerField('房间号')
    count=models.IntegerField('人数')

class UAV(models.Model):
    id = models.IntegerField('id',primary_key=True)
    a1 = models.FloatField('a1',max_length=20)
    a2 = models.FloatField('a2',max_length=20)

