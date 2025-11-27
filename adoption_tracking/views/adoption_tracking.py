from rest_framework import viewsets, filters, permissions
from adoption_tracking.models.adoption_tracking import AdoptionTracking
from adoption_tracking.serializers.adoption_tracking import AdoptionTrackingSerializer

class IsAdminOrOwnerReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_staff or obj.request.user == request.user
        return request.user.is_staff

class AdoptionTrackingViewSet(viewsets.ModelViewSet):
    queryset = AdoptionTracking.objects.all()
    serializer_class = AdoptionTrackingSerializer
    permission_classes = (IsAdminOrOwnerReadOnly,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ("status", "request__id", "request__user__username")
    ordering_fields = ("updated_at",)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return AdoptionTracking.objects.all()
        return AdoptionTracking.objects.filter(request__user=user)
