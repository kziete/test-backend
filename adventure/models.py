from django.db import models

# Create your models here.


class Vehicle(models.Model):
    name = models.CharField(max_length=32)
    max_capacity = models.FloatField()

    def can_start(self):
        # TODO: romper
        return True
