# Copyright Collab 2015-2016
# See LICENSE for details.

import os
from datetime import datetime

from admin_footer import version


SITE_ID = 1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True
    },
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'admin_footer'
]

# =============================================================================
# ADMIN FOOTER
# =============================================================================

ADMIN_FOOTER_DATA = {
    'site_url': 'https://www.example.com',
    'site_name': 'MyCompany',
    'period': '2015-{}'.format(datetime.now().year),
    'version': 'v{} - '.format(version)
}

ROOT_URLCONF = 'admin_footer.tests.urls'

SECRET_KEY = 'top_secret'

LOCAL_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.abspath('media')

# A tuple of directories where Django looks for translation files.
LOCALE_PATHS = (
    os.path.join(os.path.abspath('../locale')),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

# Logging configuration.
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOG_HANDLER = 'null'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)-6s %(name)-15s - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        }
    },
    'loggers': {
        'admin_footer': {
            'handlers': [LOG_HANDLER],
            'level': 'DEBUG'
        },
    }
}
