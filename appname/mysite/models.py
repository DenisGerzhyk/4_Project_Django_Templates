from django.db import models


class Calculates(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    sign = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.x} + {self.y}"
