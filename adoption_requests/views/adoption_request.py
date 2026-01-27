from rest_framework import viewsets, permissions, filters
from adoption_requests.models.adoption_request import AdoptionRequest
from adoption_requests.serializers.adoption_request import AdoptionRequestSerializer
from rest_framework.decorators import action

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

    def perform_update(self, serializer):
            if 'status' in serializer.validated_data and not self.request.user.is_staff:
                raise serializers.ValidationError("No tienes permiso para cambiar el estado de la solicitud.")
            serializer.save()        

    @action(detail=False, methods=['get'], url_path='my-for-pet')
    def my_for_pet(self, request):
        pet_id = request.query_params.get('pet_id')

        if not pet_id:
            return Response({"detail": "pet_id es requerido"}, status=400)

        adoption = AdoptionRequest.objects.filter(
            user=request.user,
            pet_id=pet_id
        ).first()

        if not adoption:
            return Response({"exists": False})

        serializer = self.get_serializer(adoption)
        return Response({
            "exists": True,
            "adoption": serializer.data
        })