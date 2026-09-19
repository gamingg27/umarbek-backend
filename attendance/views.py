from rest_framework import serializers, viewsets
from .models import Attendance
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset=Attendance.objects.all()
    serializer_class=AttendanceSerializer

