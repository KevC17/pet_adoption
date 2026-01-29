from django.contrib.auth.models import User
from rest_framework import serializers
from users.services.email_service import send_welcome_email

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ('username','email','password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        if user.email:
            send_welcome_email(user)
        return user
