from rest_framework import serializers, viewsets
from .models import Report
class ReportViewSet(viewsets.ModelViewSet):
    queryset=Report.objects.all()
    serializer_class=ReportSerializer

