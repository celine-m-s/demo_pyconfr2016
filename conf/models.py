from django.db import models


class Speaker(models.Model):
    name = models.CharField(max_length=100)


class Talk(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    speaker = models.ForeignKey(Speaker)
