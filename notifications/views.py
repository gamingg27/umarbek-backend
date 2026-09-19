from rest_framework import serializers, viewsets
from .models import Notification
class NotificationViewSet(viewsets.ModelViewSet):
    queryset=Notification.objects.all()
    serializer_class=NotificationSerializer

