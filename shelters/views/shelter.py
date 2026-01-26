from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
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

    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )

    filterset_fields = ('is_active',)

    search_fields = ('name', 'address', 'phone')

    ordering_fields = ('name',)
