from rest_framework import serializers
from adoption_requests.models.adoption_request import AdoptionRequest

class AdoptionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptionRequest
        fields = '__all__'
        read_only_fields = ('id', 'user', 'request_date', 'status')
