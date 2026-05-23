from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    filter_class = models.CharField(max_length=50)
    image = models.CharField(max_length=255)  # Path to thumbnail
    
    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES, default='image')
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
