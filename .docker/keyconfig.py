import os

class Database:
    NAME = os.getenv('POSTGRES_DB')
    USER = os.getenv('POSTGRES_USER')
    PASSWORD = os.getenv('POSTGRES_PASSWORD')
    HOST = os.getenv('DATABASE_HOST')
    PORT = os.getenv('DATABASE_PORT')

class Secrets:
    SECRET_KEY = os.getenv('SECRET_KEY')

class Email:
    DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
    SERVER_EMAIL = os.getenv('SERVER_EMAIL')
    EMAIL_SUBJECT_PREFIX = os.getenv('EMAIL_SUBJECT_PREFIX')

class Debug:
    if os.getenv('DEBUG') == 'True':
        DEBUG = True
    else:
        DEBUG = False

class Celery:
    BROKER_URL = os.getenv('CELERY_BROKER_URL')
    RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND ')
