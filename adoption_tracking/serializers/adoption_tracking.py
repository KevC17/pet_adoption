from rest_framework import serializers
from adoption_tracking.models.adoption_tracking import AdoptionTracking

class AdoptionTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptionTracking
        fields = "__all__"
        read_only_fields = ("id", "updated_at")
