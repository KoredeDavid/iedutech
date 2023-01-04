from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if os.environ.get('DEBUG', False) == 'True' else False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '')

ALLOWED_HOSTS = ['iedutech.up.railway.app', 'iedutech.herokuapp.com', '127.0.0.1']

# os.environ.get('WEB_URL', "")

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware', )

BASE_DIR = os.getcwd()

# DATABASE settings uses sqlite when sqlite is set to true but uses Postgres if not
sqlite = True

if sqlite:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            # 'NAME': '',
            # 'USER': 'postgres',
            'PASSWORD': '',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }

# Allows error log to be shown in console when Debug = False
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] '
                       'pathname=%(pathname)s lineno=%(lineno)s '
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
# EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL')

SERVER_EMAIL = os.environ.get('SERVER_EMAIL', "")
DEFAULT_FROM_EMAIL = SERVER_EMAIL

ADMINS = [
    ('KoredeDavid', os.environ.get('EMAIL_HOST_USER', "")),
    ('Conceal', SERVER_EMAIL),
]

MANAGERS = ADMINS

if not sqlite:
    import dj_database_url

    prod_db = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(prod_db)
