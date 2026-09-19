from rest_framework import serializers, viewsets
from .models import Payment, Salary
from .serializers import *
class PaymentViewSet(viewsets.ModelViewSet):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer

class SalaryViewSet(viewsets.ModelViewSet):
    queryset=Salary.objects.all()
    serializer_class=SalarySerializer

