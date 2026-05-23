from django.contrib import admin
from .models import Project, ProjectOverview, ProjectFeature

class ProjectOverviewInline(admin.TabularInline):
    model = ProjectOverview
    extra = 1

class ProjectFeatureInline(admin.TabularInline):
    model = ProjectFeature
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date')
    inlines = [ProjectOverviewInline, ProjectFeatureInline]
