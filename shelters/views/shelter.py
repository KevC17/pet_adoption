from rest_framework import viewsets, permissions, filters
from shelters.models.shelter import Shelter
from shelters.serializers.shelter import ShelterSerializer

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff

class ShelterViewSet(viewsets.ModelViewSet):
    queryset = Shelter.objects.all().order_by('id')
    serializer_class = ShelterSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', 'address', 'phone')
    ordering_fields = ('name',)
