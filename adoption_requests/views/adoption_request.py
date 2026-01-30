from rest_framework import viewsets, permissions, filters, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status as http_status
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
        queryset = AdoptionRequest.objects.select_related('user', 'pet')
        
        if self.request.user.is_staff:
            return queryset.all()
        return queryset.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        pet = serializer.validated_data['pet']

        if pet.status == pet.Status.ADOPTED:
            raise serializers.ValidationError(
                {"pet": "No se puede solicitar adopción de una mascota ya adoptada."}
            )

        try:
            serializer.save(user=self.request.user)
        except IntegrityError:
            raise serializers.ValidationError(
                {"detail": "Ya has enviado una solicitud para esta mascota."}
            )
    
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
        ).select_related('user', 'pet').first()
        
        if not adoption:
            return Response({"exists": False})
        
        serializer = self.get_serializer(adoption)
        return Response({
            "exists": True,
            "adoption": serializer.data
        })
    
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAdminUser])
    def approve(self, request, pk=None):
        adoption = self.get_object()
        pet = adoption.pet

        if adoption.status != AdoptionRequest.Status.PENDING:
            return Response(
                {"detail": "Solo se pueden aprobar solicitudes pendientes."},
                status=http_status.HTTP_400_BAD_REQUEST
            )

        if pet.status == pet.Status.ADOPTED:
            return Response(
                {"detail": "Esta mascota ya fue adoptada."},
                status=http_status.HTTP_400_BAD_REQUEST
            )

        adoption.status = AdoptionRequest.Status.APPROVED
        adoption.save()

        AdoptionRequest.objects.filter(
            pet=pet
        ).exclude(id=adoption.id).update(
            status=AdoptionRequest.Status.REJECTED
        )
        pet.status = pet.Status.ADOPTED
        pet.save()

        return Response(
            {"detail": "Adoption approved successfully"},
            status=http_status.HTTP_200_OK
        )

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAdminUser])
    def reject(self, request, pk=None):
        adoption = self.get_object()

        if adoption.status != AdoptionRequest.Status.PENDING:
            return Response(
                {"detail": "Solo se pueden rechazar solicitudes pendientes."},
                status=http_status.HTTP_400_BAD_REQUEST
            )

        adoption.status = AdoptionRequest.Status.REJECTED
        adoption.save()

        return Response(
            {"detail": "Adoption rejected successfully"},
            status=http_status.HTTP_200_OK
        )