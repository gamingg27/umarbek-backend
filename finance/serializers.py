from rest_framework import serializers, viewsets
from .models import Payment, Salary
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields='__all__'

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model=Salary
        fields='__all__'

