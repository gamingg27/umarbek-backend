from rest_framework import serializers, viewsets
from .models import Attendance
from .serializers import *
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset=Attendance.objects.all()
    serializer_class=AttendanceSerializer

