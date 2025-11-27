from django.db import models
from django.utils import timezone
from adoption_requests.models.adoption_request import AdoptionRequest

class AdoptionTracking(models.Model):
    request = models.OneToOneField(AdoptionRequest, on_delete=models.CASCADE, related_name="tracking")
    status = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-updated_at",)

    def __str__(self):
        return f"Tracking for Request #{self.request.id}"
