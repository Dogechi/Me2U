"""
Django settings for Me2U project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import boto3
import django_heroku
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from botocore.config import Config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = bool(os.environ.get('LOCAL_DEBUG', ''))
DEBUG = True


REDIS_URL = os.environ.get('REDIS_URL')

ALLOWED_HOSTS = ['https://me2uafrica.herokuapp.com/', 'http://127.0.0.1:8000/']
CANON_URL_HOST = 'me2uafrica.herokuapp.com/'
CANON_URLS_TO_REWRITE = ['me2u-africa.com', 'www.me2uafricaherokuapp.com']

s3 = boto3.client('s3', config=Config(signature_version='s3v4'))

# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'channels',
    # 'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.redirects',
    'django_extensions',
    'django_filters',
    'debug_toolbar',
    'widget_tweaks',
    'django_tables2',
    'django.contrib.sitemaps',
    'main',
    'bootstrap3',
    'users.apps.UsersConfig',
    'categories',
    'me2ushop',
    'crispy_forms',
    'django_countries',
    'stripe',
    'utils',
    'search',
    'sellers',
    'stdimage',
    'stats',
    'tagging',
    'storages',
    'rest_framework',
    'rest_framework.authtoken',
    'webpack_loader',

]
DJANGO_TABLES2_TEMPLATE = 'django_tables2/bootstrap.html'

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':
        ('rest_framework.authentication.SessionAuthentication',
         'rest_framework.authentication.TokenAuthentication',
         'rest_framework.authentication.BasicAuthentication',

         ),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.DjangoModelPermissions',),
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination', 'PAGE_SIZE': 100

}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'Me2U.SSLMiddleware.SSLRedirect',
    'main.middleware.cart_middleware',
    # 'marketing.urlcanon.URLCanonicalizationMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware'

]
INTERNAL_IPS = ['127.0.0.1']

ROOT_URLCONF = 'Me2U.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'utils.context_processors.me2u',
                'utils.context_processors.globals',
            ],

        },
    },
]
WEBPACK_LOADER = {
    'DEFAULT': {'BUNDLE_DIR_NAME': 'bundles/',
                'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
                }
}

WSGI_APPLICATION = 'Me2U.wsgi.application'
ASGI_APPLICATION = 'Me2U.routing.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [REDIS_URL],
        },
    },
}
SITE_ID = 1
GA_TRACKER_ID = '123'
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'me2u',
#         'USER': os.environ.get('USER'),
#         'PASSWORD': os.environ.get('PASSWORD'),
#         'HOST': 'localhost',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

SITE_NAME = 'Me2U|Africa'
META_KEYWORDS = 'ONLINE MARKET, RWANDA ECOMMERCE, OLANDO, SHYPT,IKUKU,BUY ONLINE'
META_DESCRIPTION = 'Me2U|Africa is an online self sustaining ecommerce tailored towards delivering best services and ' \
                   'products' \
                   'Across the globe with a major focus in African markets.'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'me2ushop:home'
LOGIN_URL = 'login'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_STORAGE = 'Me2U.storage.WhiteNoiseStaticFilesStorage'

# stripe settings

if DEBUG:
    # test keys
    STRIPE_PUBLISHABLE_kEY = os.environ.get('STRIPE_PUBLISHABLE_kEY')
    STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    STRIPE_PUBLISHABLE_kEY = os.environ.get('STRIPE_PUBLISHABLE_kEY')
    STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
    # Email Config
    # Email server
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST_USER = "Daniel Makori"
    EMAIL_HOST = "smtp.domain.com"
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_PASSWORD = os.environ.get('PASSWORD')

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

ADMINS = (
    ('Me2U|Africa IT', 'danielmakori0@gmail.com'),
)

EMAIL_SUBJECT_PREFIX = '[Me2U|Africa]'

PRODUCTS_PER_PAGE = 4
PRODUCTS_PER_ROW = 12

AUTH_PROFILE_MODULE = 'users.profile'
AUTH_USER_MODEL = 'users.User'


# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True


try:
    from settings_local import *
except ImportError:
    pass

# turn to true during production
# ENABLE_SSL = False

# Activate Django-Heroku.
django_heroku.settings(locals())
