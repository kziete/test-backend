from django.db import models

# Create your models here.


class Vehicle(models.Model):
    max_capacity = models.FloatField()

    def can_start(self):
        # TODO: romper
        return True
