from rest_framework import serializers, viewsets
from .models import Student, Teacher, Course, Group
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields='__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields='__all__'

