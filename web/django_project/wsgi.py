"""
WSGI config for django_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import pathlib
from django.core.wsgi import get_wsgi_application
import dotenv

CURRENT_DIR = pathlib.Path(__file__).resolve().parent.parent
ENV_DIR = CURRENT_DIR / ".env"
dotenv.read_dotenv(str(ENV_DIR))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

application = get_wsgi_application()
