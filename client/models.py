from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)

    def __str__(self):
        return self.name
