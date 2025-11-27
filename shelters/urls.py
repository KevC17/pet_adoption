from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shelters.views.shelter import ShelterViewSet

router = DefaultRouter()
router.register(r'shelters', ShelterViewSet, basename='shelters')

urlpatterns = [
    path('', include(router.urls)),
]
