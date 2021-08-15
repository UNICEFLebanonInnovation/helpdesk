"""
Django settings for django-helpdesk demodesk project.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# import environ
#
# env = environ.Env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_crkn1+fnzu5$vns_-d+^ayiq%z4k*s!!ag0!mfy36(y!vrazd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['unicef-helpdesk.herokuapp.com', '127.0.0.1', 'interagency.herokuapp.com', 'covid-vaccine-info.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'survey.apps.SuitConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
    'bootstrap4form',
    'helpdesk',
    'survey',
    'anymail',
    'sendgrid',
    'reversion',
    'import_export',
    'django_filters',
    'django_tables2',
    'bootstrap4',
    # 'tinymce',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            # str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                # Your stuff: custom template context processors go here
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# django-helpdesk configuration settings
# You can override django-helpdesk's defaults by redefining them here.
# To see what settings are available, see the docs/configuration.rst
# file for more information.
# Some common settings are below.

HELPDESK_DEFAULT_SETTINGS = {
            'use_email_as_submitter': True,
            'email_on_ticket_assign': True,
            'email_on_ticket_change': True,
            'login_view_ticketlist': True,
            'email_on_ticket_apichange': True,
            'preset_replies': True,
            'tickets_per_page': 25
}

# Should the public web portal be enabled?
HELPDESK_PUBLIC_ENABLED = False
HELPDESK_VIEW_A_TICKET_PUBLIC = False
HELPDESK_SUBMIT_A_TICKET_PUBLIC = False

# Should the Knowledgebase be enabled?
HELPDESK_KB_ENABLED = False

# Allow users to change their passwords
HELPDESK_SHOW_CHANGE_PASSWORD = True

# Instead of showing the public web portal first,
# we can instead redirect users straight to the login page.
HELPDESK_REDIRECT_TO_LOGIN_BY_DEFAULT = True
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

# Database
# - by default, we use SQLite3 for the demo, but you can also
#   configure MySQL or PostgreSQL, see the docs for more:
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    # 'default': os.environ.get('DATABASE_URL', default='postgres:///postgres'),
# }
# DATABASES['default']['ATOMIC_REQUESTS'] = True

# DATABASES = {"default": os.environ.get("DATABASE_URL", "postgres:///postgres")}
# DATABASES["default"]["ATOMIC_REQUESTS"] = True

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('DATABASE_URL', "postgres:///postgres"),
#     }
# }

# DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.postgresql',
#          'NAME': 'survey',
#          'USER': 'postgres',
#          'PASSWORD': '',
#          'HOST': 'localhost',
#          'PORT': '5432',
#      }
# }

# DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.postgresql',
#          'NAME': 'd610a40e1q2d8j',
#          'USER': 'fgbacohzpjuxxx',
#          'PASSWORD': 'a6d3df7ed4e15cd122aa317df727be7a297db557019c269be507eb6996730622',
#          'HOST': 'ec2-54-217-225-16.eu-west-1.compute.amazonaws.com',
#          'PORT': '5432',
#      }
# }

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': 'd67qehgg5a74iv',
         'USER': 'ftxkvbirafznct',
         'PASSWORD': 'e49962e569fb4d755b3d70c8c95719a65cedccc9327683afd24bf71496ea1248',
         'HOST': 'ec2-54-217-206-236.eu-west-1.compute.amazonaws.com',
         'PORT': '5432',
     }
}

# Sites
# - this allows hosting of more than one site from a single server,
#   in practice you can probably just leave this default if you only
#   host a single site, but read more in the docs:
# https://docs.djangoproject.com/en/1.11/ref/contrib/sites/

SITE_ID = 1


# Sessions
# https://docs.djangoproject.com/en/1.11/topics/http/sessions

SESSION_COOKIE_AGE = 86400  # = 1 day

# For better default security, set these cookie flags, but
# these are likely to cause problems when testing locally
#CSRF_COOKIE_SECURE = True
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_HTTPONLY = True
#SESSION_COOKIE_HTTPONLY = True


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



# STORAGE CONFIGURATION
# ------------------------------------------------------------------------------
# Uploaded Media Files
# ------------------------
# See: http://django-storages.readthedocs.io/en/latest/index.html
INSTALLED_APPS += ['storages', ]

AZURE_ACCOUNT_NAME = os.environ.get('AZURE_ACCOUNT_NAME', default='NO_AZURE_ACCOUNT_NAME')
AZURE_ACCOUNT_KEY = os.environ.get('AZURE_ACCOUNT_KEY', default='NO_AZURE_ACCOUNT_KEY')
AZURE_CONTAINER = os.environ.get('AZURE_CONTAINER', default='NO_AZURE_CONTAINER')

# DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
# DEFAULT_FILE_FORMAT = 'xlsx'
# DEFAULT_FILE_CONTENT_TYPE = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
# DEFAULT_FILE_CONTENT_LANGUAGE = 'ar'

# Email
# https://docs.djangoproject.com/en/1.11/topics/email/

# This demo uses the console backend, which simply prints emails to the console
# rather than actually sending them out.
# DEFAULT_FROM_EMAIL = 'postmaster@sandbox0253ea7b8ba44ff49d19b054fdb26e39.mailgun.org'
# SERVER_EMAIL = 'postmaster@sandbox0253ea7b8ba44ff49d19b054fdb26e39.mailgun.org'

# Anymail with Mailgun
# ANYMAIL = {
#     'MAILGUN_API_KEY': os.environ.get('MAILGUN_API_KEY', default='NO KEY'),
#     'MAILGUN_DOMAIN': os.environ.get('MAILGUN_DOMAIN', default='NO_DOMAIN'),
#     'MAILGUN_SENDER_DOMAIN': os.environ.get('MAILGUN_SENDER_DOMAIN', default='NO_SENDER_DOMAIN')
# }
# EMAIL_BACKEND = 'anymail.backends.mailgun.MailgunBackend'
# MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY', default='NO KEY')
# MAILGUN_DOMAIN = os.environ.get('MAILGUN_DOMAIN', default='NO DOMAIN')

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# If you want to test sending real emails, uncomment and modify the following:
# EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
# EMAIL_HOST = os.environ.get('MAILGUN_SMTP_SERVER', default='smtp.example.com')
# EMAIL_PORT = os.environ.get('MAILGUN_SMTP_PORT', default=25)


SENDGRID_PASSWORD = os.environ.get('SENDGRID_PASSWORD', default='NO_PASSWORD')
SENDGRID_USERNAME = os.environ.get('SENDGRID_USERNAME', default='NO_USERNAME')
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY', default='NO_API_KEY')


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# By default, django-helpdesk uses en, but other languages are also available.
# The most complete translations are: es-MX, ru, zh-Hans
# Contribute to our translations via Transifex if you can!
# See CONTRIBUTING.rst for more info.

LANGUAGE_COOKIE_NAME = 'default_language'
# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'ar-ar'

LANGUAGES = (
    ('ar-ar', 'arabic'),
    ('en-us', 'english'),
    # ('fr-fr', 'french'),
)

LANGUAGES_BIDI = ["en-us"]
# LANGUAGES_BIDI = ["ar-ar"]

LANGUAGE_COOKIE_SECURE = False
LANGUAGE_COOKIE_HTTPONLY = False
LANGUAGE_COOKIE_SAMESITE = None

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# STATIC_URL = '/static/'
# static root needs to be defined in order to use collectstatic
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# MEDIA_ROOT is where media uploads are stored.
# We set this to a directory to host file attachments created
# with tickets.
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Location of root django.contrib.admin URL, use {% url 'admin:index' %}
ADMIN_URL = r'^'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'helpdesk/locale'),
]

# Fixtures
# https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-FIXTURE_DIRS
# - This is only necessary to make the demo project work, not needed for
# your own projects unless you make your own fixtures
FIXTURE_DIRS = [os.path.join(BASE_DIR, 'fixtures')]

MODULE_HELPDESK_ACTIVE = os.environ.get('MODULE_HELPDESK_ACTIVE', default=False)
MODULE_SURVEY_ACTIVE = os.environ.get('MODULE_SURVEY_ACTIVE', default=True)

try:
    from .local_settings import *
except ImportError:
    pass