from django.contrib import admin

from projects.models import Projects

# Register your models here.

class ProjectInline(admin.TabularInline):
    model = Projects
    extra = 1    


@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'techno','image')
    list_filter = ('techno','name')
    search_fields = ('name', 'techno')