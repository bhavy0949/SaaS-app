from django.core.management.base import BaseCommand
from helpers import download_to_local
from pathlib import Path
from django.conf import settings

VENDOR_STATICFILES = {
"flowbite.min.css": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
"flowbite.min.js": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js",
}

STATICFILES_VENDOR_DIRS = getattr(settings, "STATICFILES_VENDOR_DIRS", None)

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print("Downloading static files")
        for filename, url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDOR_DIRS / filename
            success = download_to_local(url, out_path)
            if success:
                self.stdout.write(self.style.SUCCESS(f"Successfully downloaded {filename}"))
            else:
                self.stdout.write(self.style.ERROR(f"Failed to download {filename}"))