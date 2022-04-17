"""
WSGI config for midi2musicServerDjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
"""
web网关配置文件
"""
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'midi2musicServerDjango.settings')

application = get_wsgi_application()
