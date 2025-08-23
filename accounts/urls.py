# accounts/urls.py

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserRegistrationView, UserProfileView # Import the UserProfileView

urlpatterns = [
    # User authentication endpoints
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'), # DRF's built-in view for token retrieval

    # User profile management endpoint
    path('profile/', UserProfileView.as_view(), name='user-profile'), # Add this line
]