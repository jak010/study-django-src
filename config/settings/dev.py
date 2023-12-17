from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# INSTALL APPS

DOWNLOAD_APPS = [
    'django_extensions'
]
LOCAL_APPS = [
    'application'
]

INSTALLED_APPS += DOWNLOAD_APPS + LOCAL_APPS
