from rest_framework import serializers, viewsets
from .models import Notification
from .serializers import *
class NotificationViewSet(viewsets.ModelViewSet):
    queryset=Notification.objects.all()
    serializer_class=NotificationSerializer

