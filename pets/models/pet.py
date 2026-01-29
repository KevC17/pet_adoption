from django.db import models

class Pet(models.Model):

    class Status(models.TextChoices):
        AVAILABLE = 'AVAILABLE', 'Available'
        PENDING = 'PENDING', 'Pending adoption'
        ADOPTED = 'ADOPTED', 'Adopted'
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.AVAILABLE
    )
    shelter = models.ForeignKey('shelters.Shelter', on_delete=models.CASCADE)
    admission_date = models.DateField()
    is_sterilized = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='pets/',null=True,blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
