from django.contrib import admin
from .models import Endpoint
# Register your models here.

class EndpointAdmin(admin.ModelAdmin):
    list_display = ('updated_at', 'endpoint', 'project')
    # search_fields = ('restaurant_name')

admin.site.register(Endpoint, EndpointAdmin)
