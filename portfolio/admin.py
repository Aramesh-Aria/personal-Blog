from django.contrib import admin
from .models import Project, ProjectOverview, ProjectFeature, ContactMessage

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

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)
