from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
router=DefaultRouter()
router.register(r'student', StudentViewSet)
router.register(r'teacher', TeacherViewSet)
router.register(r'course', CourseViewSet)
router.register(r'group', GroupViewSet)

urlpatterns=[path('', include(router.urls))]
