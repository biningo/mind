"""
Django settings for Blog2 project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
<<<<<<< HEAD
from django.conf.global_settings import STATICFILES_DIRS
=======
<<<<<<< HEAD
from django.conf.global_settings import STATICFILES_DIRS
=======
>>>>>>> '解决用户登录和前端样式调整'
>>>>>>> '解决用户登录和前端样式调整'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> '解决用户登录和前端样式调整'
SECRET_KEY = '+qi4-m8vv%5zj2d0w0s6sn+qsnizh86p+!b4+13&=kavynkm^6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
<<<<<<< HEAD
=======
=======
SECRET_KEY = 'dsadsadq231b4+13&=kavynkm^6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
>>>>>>> '解决用户登录和前端样式调整'
>>>>>>> '解决用户登录和前端样式调整'

ALLOWED_HOSTS = ['www.binnb.top',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ArticleApp',
    'UserApp',
    'PersonalSpaceApp',
    'OtherApp',
    'MainApp',
    'AdminApp'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'Blog2.middleware.user_uid_middleware.UserAccessMiddleWare',
]

ROOT_URLCONF = 'Blog2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Blog2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

<<<<<<< HEAD

=======
<<<<<<< HEAD

=======
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog2',
        'USER': 'root',
        'PASSWORD': '55555',
        'HOST': 'localhost',
        'PORT': '3306',
	'CHARSET': 'utf8',
	'COLLATION': 'utf8_general_ci',
	
    }
}
>>>>>>> '解决用户登录和前端样式调整'
>>>>>>> '解决用户登录和前端样式调整'


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
STATIC_ROOT = os.path.join(BASE_DIR, 'collect_static')

>>>>>>> '解决用户登录和前端样式调整'
>>>>>>> '解决用户登录和前端样式调整'
STATIC_URL = '/static/'
STATICFILES_DIRS =(
        os.path.join(BASE_DIR, "static"),
)

MEDIA_URL = '/media/' #上传文件的目录
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


#邮件功能
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False   #是否使用TLS安全传输协议(用于在两个通信应用程序之间提供保密性和数据完整性。)
<<<<<<< HEAD
EMAIL_USE_SSL = False    #是否使用SSL加密，qq企业邮箱要求使用
EMAIL_HOST = 'smtp.163.com'   #发送邮件的邮箱 的 SMTP服务器，这里用了163邮箱
EMAIL_PORT = 25     #发件箱的SMTP服务器端口
=======
<<<<<<< HEAD
EMAIL_USE_SSL = False    #是否使用SSL加密，qq企业邮箱要求使用
EMAIL_HOST = 'smtp.163.com'   #发送邮件的邮箱 的 SMTP服务器，这里用了163邮箱
EMAIL_PORT = 25     #发件箱的SMTP服务器端口
=======
EMAIL_USE_SSL = True    #是否使用SSL加密，qq企业邮箱要求使用
EMAIL_HOST = 'smtp.163.com'   #发送邮件的邮箱 的 SMTP服务器，这里用了163邮箱
EMAIL_PORT = 465     #发件箱的SMTP服务器端口
>>>>>>> '解决用户登录和前端样式调整'
>>>>>>> '解决用户登录和前端样式调整'
EMAIL_HOST_USER = 'm19884605250@163.com'    #发送邮件的邮箱地址
EMAIL_HOST_PASSWORD = 'curry052530'         #发送邮件的邮箱密码(这里使用的是授权码)
