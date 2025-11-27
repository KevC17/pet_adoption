from django.urls import path, include
from rest_framework.routers import DefaultRouter
from adoption_requests.views.adoption_request import AdoptionRequestViewSet

router = DefaultRouter()
router.register(r'adoption-requests', AdoptionRequestViewSet, basename='adoption-requests')

urlpatterns = [
    path('', include(router.urls)),
]
