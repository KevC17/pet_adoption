from rest_framework_simplejwt.views import TokenObtainPairView
from users.serializers.token import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
