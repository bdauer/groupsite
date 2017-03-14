"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

try:
    from .secure import SECURE_SETTINGS
except ImportError:
    SECURE_SETTINGS = os.environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECURE_SETTINGS["SECRET_KEY"]
PRODUCTION = SECURE_SETTINGS.get("PRODUCTION", True)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'group-site-staging.pin92cyv3d.us-east-1.elasticbeanstalk.com',
                 'ip-172-31-19-100.ec2.internal', '34.206.32.33',
                 'group-site-production.pin92cyv3d.us-east-1.elasticbeanstalk.com/']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'groupsite',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    # 'social_core.backends.facebook.FacebookOAuth2',
     'django.contrib.auth.backends.ModelBackend'
)

# http://python-social-auth.readthedocs.io/en/latest/pipeline.html#authentication-pipeline
SOCIAL_AUTH_PIPELINE = ('social_core.pipeline.social_auth.social_details',
                        'social_core.pipeline.social_auth.social_uid',
                        'social_core.pipeline.social_auth.auth_allowed',
                        'social_core.pipeline.social_auth.social_user',
                        'social_core.pipeline.user.get_username',
                        'social_core.pipeline.mail.mail_validation',
                        'social_core.pipeline.social_auth.associate_by_email',
                        'social_core.pipeline.user.create_user',
                        'groupsite.pipeline.save_user',
                        'social_core.pipeline.social_auth.associate_user',
                         'social_core.pipeline.social_auth.load_extra_data',
                         'social_core.pipeline.user.user_details')

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = SECURE_SETTINGS["GOOGLE_OAUTH2_KEY"]
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = SECURE_SETTINGS["GOOGLE_OAUTH2_SECRET"]

LOGIN_REDIRECT_URL = "groupsite:index"

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
if PRODUCTION:
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': SECURE_SETTINGS['RDS_DB_NAME'],
        'USER': SECURE_SETTINGS['RDS_USERNAME'],
        'PASSWORD': SECURE_SETTINGS['RDS_PASSWORD'],
        'HOST': SECURE_SETTINGS['RDS_HOSTNAME'],
        'PORT': SECURE_SETTINGS['RDS_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if DEBUG:
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    INSTALLED_APPS += (
        'debug_toolbar',
    )
    INTERNAL_IPS = ('127.0.0.1', 'localhost')
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }
