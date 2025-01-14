from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.template.response import TemplateResponse

class CustomAdminSite(admin.AdminSite):
    site_header = "Custom Admin Dashboard"
    
    def has_permission(self, request):
        # Allow access to logged-in superusers
        return request.user.is_active and request.user.is_superuser
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('stats/', self.admin_view(self.stats_view)),
        ]
        return custom_urls + urls

    def stats_view(self, request):
        # Fetch your stats logic here
        stats = {
            'visits': 10234,
            'unique_users': 2345,
            'page_views': 56432,
        }
        return TemplateResponse(request, "stats.html", {'stats': stats})

# Instantiate and register the custom admin site
custom_admin_site = CustomAdminSite(name="custom_admin")
#custom_admin_site.register(SomeModel)  # Register your models
