from django.conf import settings
from django.db import models
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    address = models.CharField(max_length=255, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    def __str__(self): return self.user.username
