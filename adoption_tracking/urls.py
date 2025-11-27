from django.urls import path, include
from rest_framework.routers import DefaultRouter
from adoption_tracking.views.adoption_tracking import AdoptionTrackingViewSet

router = DefaultRouter()
router.register(r'adoption-tracking', AdoptionTrackingViewSet, basename='adoption-tracking')

urlpatterns = [
    path('', include(router.urls)),
]
