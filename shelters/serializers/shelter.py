from rest_framework import serializers
from shelters.models.shelter import Shelter

class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelter
        fields = '__all__'
