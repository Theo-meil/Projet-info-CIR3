from django.db import models
from django.contrib.auth.models import User

class TelemetryLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    path = models.CharField(max_length=500)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    status_code = models.IntegerField()
    response_time = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

