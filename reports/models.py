from django.db import models
class Report(models.Model):
    title=models.CharField(max_length=200)
    report_type=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    data=models.JSONField(default=dict, blank=True)
