"""
WSGI config for movie_rental project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from decouple import config

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_rental.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_rental.settings.'+config("ENVIRONMENT", default="local"))

application = get_wsgi_application()
