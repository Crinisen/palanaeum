from .keyconfig import Database, Secrets, Email, Debug, Celery

# Decide if you want to run in debug mode or not.
# Never use DEBUG mode in production!
DEBUG = Debug.DEBUG
#DEBUG = True

# Set a very secret secret key!
SECRET_KEY = Secrets.SECRET_KEY

# List your administrators
# https://docs.djangoproject.com/en/1.10/ref/settings/#admins
ADMINS = ()

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': Database.NAME,
        'USER': Database.USER,
        'PASSWORD': Database.PASSWORD,
        'HOST': Database.HOST,
        'PORT': Database.PORT,
    }
}

# Set the communication gateway for Celery
# Redis is the easiest to use.
CELERY_BROKER_URL = Celery.BROKER_URL
CELERY_RESULT_BACKEND = Celery.RESULT_BACKEND

# Configure e-mail backend
# Find more e-mail settings here:
# https://docs.djangoproject.com/en/1.10/ref/settings/#email
DEFAULT_FROM_EMAIL = Email.DEFAULT_FROM_EMAIL
SERVER_EMAIL = Email.SERVER_EMAIL
EMAIL_SUBJECT_PREFIX = Email.EMAIL_SUBJECT_PREFIX
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Set a proper cache backend
# https://docs.djangoproject.com/en/1.10/ref/settings/#caches
# I suggest using Redis with django-redis-cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        # 'BACKEND': 'redis_cache.RedisCache',
        # 'LOCATION': '/var/run/redis/redis.sock',
        # 'OPTIONS': {
        #     'DB': 1,
        #     'PASSWORD': 'yadayada',
        #     'PARSER_CLASS': 'redis.connection.HiredisParser',
        #     'PICKLE_VERSION': 2,
        # },
    },
    'search': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
    'config': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# TinyMCE API Key:
# TINYMCE_API_KEY = 'Put your key here'
