from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pets.views.pet import PetViewSet

router = DefaultRouter()
router.register(r'pets', PetViewSet, basename='pets')

urlpatterns = [
    path('', include(router.urls)),
]