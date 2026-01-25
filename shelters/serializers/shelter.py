from rest_framework import serializers
from shelters.models.shelter import Shelter

class ShelterSerializer(serializers.ModelSerializer):
    pets_count = serializers.IntegerField(source='pets.count', read_only=True)

    class Meta:
        model = Shelter
        fields = '__all__'
