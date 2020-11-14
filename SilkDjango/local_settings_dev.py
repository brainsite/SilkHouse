import os

LOCAL_SETTINGS = True
from .settings import *

DEV = True

# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# STATIC_PATH = os.path.join(BASE_DIR, 'static')
# STATIC_ROOT = '/home/skv/PycharmProjects/SilkDjango/static/'
# STATIC_URL = '/static/'
# STATICFILES_DIRS = (
#     STATIC_ROOT,
# )
# MEDIA_URL = '/media/'
# MEDIA_ROOT = '/home/skv/PycharmProjects/SilkDjango/media/'

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INTERNAL_IPS = ['127.0.0.1', ]