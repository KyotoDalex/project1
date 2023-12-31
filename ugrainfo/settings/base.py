"""
Django settings for ugrainfo project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from wagtail.embeds.oembed_providers import youtube
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/


# Application definition
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
WAGTAIL_VIDEOS_DISABLE_TRANSCODE = True

INSTALLED_APPS = [
    "home",
    "search",
    'post',
    'snippets',
    "ugrainfo",
    "forms",
    "profanity",
    "newsletter",

    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.modeladmin",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "wagtailvideos",
    'wagtail.api.v2',

    "wagtail.contrib.routable_page",

    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    'rest_framework',
    'wagtailcaptcha',
    'fontawesomefree',
    'sass_processor'
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "ugrainfo.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                'post.context_processors.breaking_news',
                'post.context_processors.last_news',
                'post.context_processors.all_posts',
                'post.context_processors.all_posts2',
                'post.context_processors.all_posts3',
                'post.context_processors.tyumen_news',
                'post.context_processors.yamal_news',
                'post.context_processors.ugra_news',
                "post.context_processors.listing",
                'post.context_processors.tyumen_listing',
                'post.context_processors.yamal_listing',
                'post.context_processors.ugra_listing',
                'post.context_processors.author_check',
                'post.context_processors.random_person',
                'post.context_processors.hmao_valid',
                'post.context_processors.yamal_valid',
                'post.context_processors.tyumen_valid',
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            "libraries": {
                'my_tag': 'snippets.template_tag.my_tag'
            }
        },
    },
]

WSGI_APPLICATION = "ugrainfo.wsgi.application"
WAGTAILEMBEDS_FINDERS = [

        {
            'class': 'wagtail.embeds.finders.oembed',
            'providers': [youtube],
            'options': {'scheme': 'https'}
        },

]
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    'sass_processor.finders.CssFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/4.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"
SASS_PROCESSOR_ROOT = STATIC_ROOT

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Wagtail settings

WAGTAIL_SITE_NAME = "ugrainfo"

# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = "http://example.com"

WAGTAIL_FRONTEND_LOGIN_TEMPLATE = 'account.html'
WAGTAIL_FRONTEND_LOGIN_URL = '/accounts/login/'
# SMTP validation
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_USE_SSL = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST_USER = 'test123123123t@yandex.ru'
EMAIL_HOST_PASSWORD = 'pdelngtnjltobace'
EMAIL_PORT = 465
DEFAULT_FROM_EMAIL = 'test123123123t@yandex.ru'
SERVER_EMAIL = EMAIL_HOST_USER

# Redis related settings

REDIS_HOST = 'localhost'
REDIS_PORT = '6379'
CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
broker_connection_retry_on_startup = True
SECRET_KEY = "django-insecure-8+(fgey3gfk39v390_%c%_h9tf4cii@as+p8a_9+$lf9uka5w1"


