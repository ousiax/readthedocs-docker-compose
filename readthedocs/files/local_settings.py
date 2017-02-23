import os


PRODUCTION_DOMAIN = 'localhost'
PRODUCTION_DOMAIN = os.environ.get('PRODUCTION_DOMAIN', PRODUCTION_DOMAIN)

SLUMBER_API_HOST = 'http://{0}'.format(PRODUCTION_DOMAIN)
SLUMBER_API_HOST = os.environ.get('SLUMBER_API_HOST', SLUMBER_API_HOST)

PUBLIC_API_URL = 'http://{0}'.format(PRODUCTION_DOMAIN)
PUBLIC_API_URL = os.environ.get('PUBLIC_API_URL', PUBLIC_API_URL)

TIME_ZONE = os.environ.get('TIME_ZONE', 'Asia/Chongqing')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', EMAIL_BACKEND)
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'localhost')
EMAIL_PORT = os.environ.get('EMAIL_PORT', 25)
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', None)
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', None)
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', EMAIL_HOST_USER)
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', None)
EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL', None)

ES_HOSTS = os.environ.get('ES_HOSTS', '127.0.0.1:9200').split(';')
ES_DEFAULT_NUM_REPLICAS = os.environ.get('ES_DEFAULT_NUM_REPLICAS', 0)
ES_DEFAULT_NUM_SHARDS = os.environ.get('ES_DEFAULT_NUM_SHARDS', 5)

ALLOW_ADMIN = eval(os.environ.get('ALLOW_ADMIN', 'False'))

DEBUG = eval(os.environ.get('DEBUG', 'False'))
