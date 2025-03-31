from typing import Any
from django.core.management.base import BaseCommand
import helpers
import os
from django.conf import settings
from pathlib import Path

VENDOR_STATICFILES = {
    "flowbite.min.js":"https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js",
    "flowbite.min.css":"https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.css"

}

STATICFILES_VENDOR_DIR = getattr(settings, 'STATICFILES_VENDOR_DIR')

class Command(BaseCommand):
    def handle(self, *arg: Any, **options: Any):
        completed_urls = []

        for name, url in VENDOR_STATICFILES.items():
            out_path = os.path.join(STATICFILES_VENDOR_DIR, name)

            dl_success = helpers.download_to_local(url, Path(out_path))
            if dl_success:
                completed_urls.append(url)
            else:
                self.stdout.write(self.style.ERROR(f"Failed to download {url}"))
        
        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(self.style.SUCCESS('Successfully downloaded'))
        else:
            self.stdout.write(self.style.WARNING('Failed to download some files'))
        