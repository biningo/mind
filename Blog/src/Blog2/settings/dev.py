from .base import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog2',
        'USER': 'root',
        'PASSWORD': '55555',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}