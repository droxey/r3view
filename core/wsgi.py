"""
WSGI config for the r3view project.
It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")


application = WhiteNoise(get_wsgi_application(), root='../static/')
application.auto_refresh = settings.DEBUG
