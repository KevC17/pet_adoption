from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from pets.models.pet import Pet
from pets.serializers.pet import PetSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff


class PetViewSet(viewsets.ModelViewSet):
    serializer_class = PetSerializer
    permission_classes = (IsAdminOrReadOnly,)

    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )

    filterset_fields = ('shelter',)
    search_fields = ('name', 'species', 'breed', 'gender', 'status')
    ordering_fields = ('name', 'age', 'admission_date')
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        queryset = Pet.objects.all().order_by('id')

        shelter_id = self.request.query_params.get('shelter')
        if shelter_id:
            queryset = queryset.filter(shelter_id=shelter_id)

        return queryset
