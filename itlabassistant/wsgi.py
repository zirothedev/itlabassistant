"""
WSGI config for itlabassistant project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'itlabassistant.settings')

application = get_wsgi_application()

app = application

# your_project_name/wsgi.py


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')

try:
    application = get_wsgi_application()
except Exception as e:
    print(f"WSGI Failed: {str(e)}", file=sys.stderr)
    raise