from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    status = models.CharField(max_length=20)
    shelter = models.ForeignKey('shelters.Shelter', on_delete=models.CASCADE)
    admission_date = models.DateField()
    photo = models.ImageField(upload_to='pets/',null=True,blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
