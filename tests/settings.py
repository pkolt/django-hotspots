import os

PROJECT_PATH = os.path.dirname(__file__)

DEBUG = True

MEDIA_ROOT = os.path.normpath(os.path.join(PROJECT_PATH, "media"))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_PATH, 'uploadtools.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'TEST_CHARSET': 'utf8',
    },
}

INSTALLED_APPS = (
    'djng.hotspots',
    'djng.hotspots.tests',
)