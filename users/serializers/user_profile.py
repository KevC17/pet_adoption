from rest_framework import serializers
from users.models.user_profile import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            'phone',
            'city',
            'address',
            'housing_type',
            'has_other_pets',
            'photo',
        )
