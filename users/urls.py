from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views.admin import UserAdminViewSet
from users.views.auth import RegisterView
from users.views.token import CustomTokenObtainPairView
from users.views.profile import UserProfileView
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'admin/users', UserAdminViewSet, basename='admin-users')

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('me/profile/', UserProfileView.as_view()),
    path('auth/login/', CustomTokenObtainPairView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
    path('', include(router.urls)),
]
