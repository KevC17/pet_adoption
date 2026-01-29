from django.db import models
from django.contrib.auth.models import User
from pets.models.pet import Pet

class AdoptionRequest(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pendiente'
        APPROVED = 'APPROVED', 'Aprobada'
        REJECTED = 'REJECTED', 'Rechazada'
        CANCELLED = 'CANCELLED', 'Cancelada'
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adoption_requests')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='adoption_requests')
    request_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20,choices=Status.choices,default=Status.PENDING)
    notes = models.TextField(blank=True)

class Meta:
    ordering = ['-request_date']
    constraints = [
        models.UniqueConstraint(
            fields=['user', 'pet'],
            name='unique_adoption_request_per_user_pet'
        )
    ]


    def __str__(self):
        return f'Request {self.id} by {self.user.username}'
