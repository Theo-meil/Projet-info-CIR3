from django.contrib import admin
from .models import TelemetryLog

@admin.register(TelemetryLog)
class TelemetryLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'user', 'path', 'status_code', 'response_time', 'ip_address')
    list_filter = ('status_code', 'timestamp')
    search_fields = ('path', 'user__username', 'ip_address')
