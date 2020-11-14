import os

LOCAL_SETTINGS = True
from .settings import *

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATIC_PATH = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = '/home/www-data/silkdjango_static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    STATIC_PATH,
)
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/www-data/silkdjango_media/'



DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'silkdjango',
            'USER': 'silkdjango',
            'PASSWORD': 'eR2NJspbzI',
            'HOST': 'localhost',
            'PORT': '5432',
    }
}

# solr-thumbnail related settings
# THUMBNAIL_FORMAT = 'PNG'
THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
THUMBNAIL_REDIS_HOST = 'localhost'
THUMBNAIL_REDIS_PORT = 6379