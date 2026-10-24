from pathlib import Path

from django.core.files import File
from django.core.files.storage import default_storage
from django.core.management.base import BaseCommand

SEED_MEDIA_DIR = Path(__file__).resolve().parents[2] / 'seed_media'


class Command(BaseCommand):
    help = 'Copies the default media files (project, profile, resume) into MEDIA_ROOT, skipping files that already exist'

    def handle(self, *args, **kwargs):
        copied = skipped = 0
        for source in sorted(SEED_MEDIA_DIR.rglob('*')):
            if not source.is_file() or source.name.startswith('.'):
                continue
            name = source.relative_to(SEED_MEDIA_DIR).as_posix()
            if default_storage.exists(name):
                skipped += 1
                continue
            with source.open('rb') as f:
                default_storage.save(name, File(f))
            copied += 1
            self.stdout.write(f'Copied {name}')

        self.stdout.write(self.style.SUCCESS(f'Media seeded: {copied} copied, {skipped} already present'))
