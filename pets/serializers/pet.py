from rest_framework import serializers
from pets.models.pet import Pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'
