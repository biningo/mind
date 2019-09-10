"""
WSGI config for Blog2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Blog2.settings')
=======
<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Blog2.settings')
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Blog2.settings.base')
>>>>>>> '解决用户登录和前端样式调整'
>>>>>>> '解决用户登录和前端样式调整'

application = get_wsgi_application()
