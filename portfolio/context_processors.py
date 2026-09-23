from datetime import datetime
from django.conf import settings


def current_year(request):
    return {
        'current_year': datetime.now().year
    }


def site_meta(request):
    site_url = getattr(settings, 'SITE_URL', 'http://localhost:8000')
    static_url = getattr(settings, 'STATIC_URL', '/static/')
    media_url = getattr(settings, 'MEDIA_URL', '/media/')
    return {
        'SITE_URL': site_url,
        'STATIC_URL': static_url,
        'MEDIA_URL': media_url,
        'default_og_title': 'Aria Aramesh — Backend Developer',
        'default_og_description': 'Backend developer focused on Python, Django, and PostgreSQL. Building real-world applications from idea to production.',
        'default_og_image': 'img/og-image.webp',
        'default_og_image_full': f"{site_url}{static_url}img/og-image.webp",
        'default_og_url': f"{site_url}/",
        'default_og_type': 'website',
    }
