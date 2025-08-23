from django.shortcuts import render

# Create your views here.
# accounts/views.py

# accounts/views.py

from rest_framework import generics, permissions
from .serializers import UserRegistrationSerializer, UserProfileSerializer
from .models import User

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # This ensures the view only operates on the authenticated user's profile
        return self.request.user