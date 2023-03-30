from django.db import models

class ToDo(models.Model):
    actividade = models.CharField(max_length=120)
    status = models.BooleanField(default=False)
