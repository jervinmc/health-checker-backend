from django.contrib import admin
from .models import Project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('updated_at', 'project_name')
    # search_fields = ('restaurant_name')

admin.site.register(Project, ProjectAdmin)
