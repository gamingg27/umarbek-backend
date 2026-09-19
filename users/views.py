from rest_framework import serializers, viewsets
from .models import UserProfile
from .serializers import *
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer

