from rest_framework import viewsets, permissions, filters
from adoption_requests.models.adoption_request import AdoptionRequest
from adoption_requests.serializers.adoption_request import AdoptionRequestSerializer

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.user == request.user

class AdoptionRequestViewSet(viewsets.ModelViewSet):
    serializer_class = AdoptionRequestSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrAdmin)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('status', 'notes')
    ordering_fields = ('request_date',)

    def get_queryset(self):
        if self.request.user.is_staff:
            return AdoptionRequest.objects.all()
        return AdoptionRequest.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
