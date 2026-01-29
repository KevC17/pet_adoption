from rest_framework import serializers
from adoption_requests.models.adoption_request import AdoptionRequest

class AdoptionRequestSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    user_email = serializers.EmailField(source='user.email', read_only=True)
    pet_name = serializers.CharField(source='pet.name', read_only=True)
    pet_species = serializers.CharField(source='pet.species', read_only=True)
    
    class Meta:
        model = AdoptionRequest
        fields = [
            'id', 'user', 'pet', 'status', 'request_date', 'notes',
            'user_name', 'user_email', 'pet_name', 'pet_species'
        ]
        read_only_fields = ['request_date', 'user']

    def validate_status(self, value):
        value = value.upper()
        valid_statuses = [
            AdoptionRequest.Status.PENDING,
            AdoptionRequest.Status.APPROVED,
            AdoptionRequest.Status.REJECTED,
            AdoptionRequest.Status.CANCELLED,
        ]

        if value not in valid_statuses:
            raise serializers.ValidationError("Estado de adopción inválido.")

        return value       