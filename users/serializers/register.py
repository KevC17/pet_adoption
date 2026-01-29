from django.contrib.auth.models import User
from rest_framework import serializers
from users.services.email_service import send_welcome_email
import logging

logger = logging.getLogger(__name__)


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        if user.email:
            try:
                send_welcome_email(user)
            except Exception as e:
                logger.error(f'Error enviando correo a {user.email}: {e}')

        return user
