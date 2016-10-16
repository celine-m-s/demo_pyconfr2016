from django.db import models


class Speaker(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        # Overcharges to show the name directly in the admin instead of Speaker object.
        return self.name


class Talk(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    speaker = models.ForeignKey(Speaker)
