from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    filter_class = models.CharField(max_length=50)
    image = models.CharField(max_length=255)  # Path to thumbnail
    og_image = models.CharField(max_length=255, blank=True, null=True, help_text="Custom Open Graph image (1200x630). Falls back to thumbnail.")
    
    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('placeholder', 'Placeholder (no media yet)'),
    ]
    media_type = models.CharField(max_length=11, choices=MEDIA_TYPE_CHOICES, default='image')
    media_src = models.CharField(max_length=255)
    media_poster = models.CharField(max_length=255, blank=True, null=True)
    
    date = models.CharField(max_length=50)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class ProjectOverview(models.Model):
    project = models.ForeignKey(Project, related_name='overview_points', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Overview for {self.project.title}"

class ProjectFeature(models.Model):
    project = models.ForeignKey(Project, related_name='features', on_delete=models.CASCADE)
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"Feature: {self.title} for {self.project.title}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=120)
    subject = models.CharField(max_length=120)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"


def resume_upload_to(instance, filename):
    from django.utils import timezone
    timestamp = timezone.now().strftime('%Y%m%d_%H%M%S')
    name, ext = filename.rsplit('.', 1)
    return f'resumes/{name}_{timestamp}.{ext}'


class Resume(models.Model):
    title = models.CharField(max_length=200, default='Resume')
    file = models.FileField(upload_to=resume_upload_to)
    date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'

    def __str__(self):
        return f"{self.title} ({'Active' if self.is_active else 'Inactive'})"

    def save(self, *args, **kwargs):
        if self.is_active:
            Resume.objects.exclude(pk=self.pk).filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    @property
    def file_size(self):
        if self.file:
            return self.file.size
        return 0

    @property
    def file_extension(self):
        if self.file:
            return self.file.name.split('.')[-1].lower()
        return ''
