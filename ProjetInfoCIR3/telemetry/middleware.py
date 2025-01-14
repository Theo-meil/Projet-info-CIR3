import time
from .models import TelemetryLog

class TelemetryMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        user = request.user if request.user.is_authenticated else None
        ip = request.META.get('REMOTE_ADDR', 'Unknown')
        user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown')
        
        response = self.get_response(request)
        
        duration = time.time() - start_time
        # Save telemetry data
        TelemetryLog.objects.create(
            user=user,
            path=request.path,
            ip_address=ip,
            user_agent=user_agent,
            status_code=response.status_code,
            response_time=duration,
        )
        
        return response
