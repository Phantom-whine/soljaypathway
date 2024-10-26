import os
from django.http import HttpResponse
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

class StaticFilesMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Check if the request path starts with STATIC_URL
        if request.path.startswith(settings.STATIC_URL):
            # Construct the full path to the static file
            static_file_path = os.path.join(settings.STATIC_ROOT, request.path[len(settings.STATIC_URL):])
            
            # Check if the file exists
            if os.path.exists(static_file_path):
                # Open the file and return it as a response
                with open(static_file_path, 'rb') as f:
                    return HttpResponse(f.read(), content_type='application/octet-stream')

        # If the static file is not found, continue to the next middleware
        return None
