from django.conf import settings
from django.db import models

class Student(models.Model):
    STATUS = [("active","Active"),("inactive","Inactive"),("graduated","Graduated")]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default="active")
    address = models.CharField(max_length=255, blank=True)
    parent_name = models.CharField(max_length=150, blank=True)
    parent_phone = models.CharField(max_length=30, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.first_name} {self.last_name}"

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    specialization = models.CharField(max_length=150, blank=True)
    salary_type = models.CharField(max_length=20, choices=[("fixed","Fixed"),("hourly","Hourly"),("percentage","Percentage")], default="fixed")
    salary_rate = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    def __str__(self): return f"{self.first_name} {self.last_name}"

class Course(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    duration_months = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    def __str__(self): return self.name

class Group(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="groups")
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name="groups")
    students = models.ManyToManyField(Student, blank=True, related_name="groups")
    room = models.CharField(max_length=100, blank=True)
    schedule = models.CharField(max_length=255, blank=True)
    start_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    def __str__(self): return self.name
