from rest_framework import serializers
from pets.models.pet import Pet

class PetSerializer(serializers.ModelSerializer):
    shelter_name = serializers.CharField(source='shelter.name', read_only=True)
    
    class Meta:
        model = Pet
        fields = '__all__'
