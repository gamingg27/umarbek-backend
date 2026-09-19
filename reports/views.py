from rest_framework import serializers, viewsets
from .models import Report
from .serializers import *
class ReportViewSet(viewsets.ModelViewSet):
    queryset=Report.objects.all()
    serializer_class=ReportSerializer

