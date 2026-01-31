from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from pets.models.pet import Pet
from pets.serializers.pet import PetSerializer
from pets.filters import PetFilter  # NUEVA LÍNEA
from rest_framework.parsers import (
    MultiPartParser,
    FormParser,
    JSONParser,
)

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    filterset_class = PetFilter
    search_fields = ('name', 'species', 'breed', 'gender', 'status')
    ordering_fields = ('name', 'age', 'admission_date')
    parser_classes = (MultiPartParser, FormParser, JSONParser)