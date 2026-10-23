from django.contrib import admin
from django.contrib import messages
from django.utils.html import format_html
from .models import Project, ProjectOverview, ProjectFeature, ContactMessage, Resume

class ProjectOverviewInline(admin.TabularInline):
    model = ProjectOverview
    extra = 1

class ProjectFeatureInline(admin.TabularInline):
    model = ProjectFeature
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'thumbnail_preview')
    inlines = [ProjectOverviewInline, ProjectFeatureInline]
    readonly_fields = ('thumbnail_preview', 'media_preview')
    fieldsets = (
        (None, {'fields': ('title', 'category', 'filter_class', 'date', 'url')}),
        ('Media', {'fields': (
            'image', 'thumbnail_preview',
            'media_type', 'media_src', 'media_poster', 'media_preview',
            'og_image',
        )}),
    )

    def thumbnail_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 120px;">', obj.image.url)
        return "-"
    thumbnail_preview.short_description = 'Thumbnail'

    def media_preview(self, obj):
        if not obj.media_src:
            return "-"
        if obj.media_type == 'video':
            return format_html('<video src="{}" style="max-height: 200px;" controls preload="metadata"></video>', obj.media_src.url)
        return format_html('<img src="{}" style="max-height: 200px;">', obj.media_src.url)
    media_preview.short_description = 'Media Preview'

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_active', 'file_size_display', 'file_extension')
    list_filter = ('is_active', 'date')
    readonly_fields = ('date', 'file_size_display', 'file_extension')
    fields = ('title', 'file', 'is_active', 'date', 'file_size_display', 'file_extension')

    def file_size_display(self, obj):
        if obj.file and not obj.file_exists:
            return "File missing - please re-upload"
        if obj.file:
            size = obj.file.size
            if size < 1024:
                return f"{size} B"
            elif size < 1024 * 1024:
                return f"{size / 1024:.1f} KB"
            else:
                return f"{size / (1024 * 1024):.1f} MB"
        return "-"
    file_size_display.short_description = 'File Size'

    def file_extension(self, obj):
        if obj.file:
            return obj.file.name.split('.')[-1].lower()
        return "-"
    file_extension.short_description = 'Type'

    def save_model(self, request, obj, form, change):
        if obj.file and not obj.file_exists and 'file' not in form.changed_data:
            messages.error(request, "The resume file is missing from storage. Please upload it again.")
            return
        if obj.file and obj.file.size > 5 * 1024 * 1024:
            messages.error(request, "File size must be less than 5MB.")
            return
        if obj.file and not obj.file.name.lower().endswith('.pdf'):
            messages.error(request, "Only PDF files are allowed.")
            return
        super().save_model(request, obj, form, change)
