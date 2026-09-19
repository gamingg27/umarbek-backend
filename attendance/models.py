from django.db import models
from education.models import Student, Group

class Attendance(models.Model):
    STATUS = [("present","Present"),("absent","Absent"),("late","Late"),("excused","Excused")]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="attendance")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="attendance")
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS, default="present")
    note = models.CharField(max_length=255, blank=True)
    class Meta:
        unique_together = ("student","group","date")
