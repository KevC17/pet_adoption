from django.db import models
from django.contrib.auth.models import User
from pets.models.pet import Pet

class AdoptionRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adoption_requests')
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='adoption_requests')
    request_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-request_date']

    def __str__(self):
        return f'Request {self.id} by {self.user.username}'
