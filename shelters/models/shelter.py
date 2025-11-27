from django.db import models

class Shelter(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
