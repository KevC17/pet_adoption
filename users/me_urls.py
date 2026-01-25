from django.urls import path
from users.views.profile import UserProfileView

urlpatterns = [
    path('me/profile/', UserProfileView.as_view(), name='user-profile'),
]
