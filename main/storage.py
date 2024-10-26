import os
from django.core.files.storage import Storage
from django.conf import settings

class CustomStaticStorage(Storage):
    def _save(self, name, content):
        # Define the full path to save the file
        full_path = os.path.join(settings.STATIC_ROOT, name)
        # Create any necessary directories
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        # Write the content to the file
        with open(full_path, 'wb+') as destination:
            for chunk in content.chunks():
                destination.write(chunk)
        return name

    def url(self, name):
        # Return the URL to the static file
        return os.path.join(settings.STATIC_URL, name)

    def exists(self, name):
        # Check if the file exists
        return os.path.exists(os.path.join(settings.STATIC_ROOT, name))

    def delete(self, name):
        # Delete the static file
        try:
            os.remove(os.path.join(settings.STATIC_ROOT, name))
        except FileNotFoundError:
            pass
