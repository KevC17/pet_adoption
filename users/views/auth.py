from rest_framework import generics, permissions
from django.contrib.auth.models import User
from users.serializers.register import RegisterSerializer
from users.models import UserProfile

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        serializer.save()  

