from django.conf import settings
from django.db import models
from education.models import Student, Course, Teacher, Group

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="payments")
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)
    method = models.CharField(max_length=30, choices=[("cash","Cash"),("card","Card"),("transfer","Transfer")], default="cash")
    status = models.CharField(max_length=20, choices=[("paid","Paid"),("pending","Pending"),("cancelled","Cancelled")], default="paid")
    note = models.TextField(blank=True)

class Salary(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="salaries")
    month = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=[("pending","Pending"),("paid","Paid")], default="pending")
    note = models.TextField(blank=True)
