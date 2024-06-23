"""
Django settings for edutech_io project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
from django.contrib.messages import constants as messages

# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("PROJECT_KEY", default="")

# SECURITY WARNING: don't run with debug turned on in production!
if os.getenv("DEBUGE_MODE") == 'True':
    DEBUG = True
else:
    DEBUG = False
    

ALLOWED_HOSTS = ['*']

MESSAGE_TAGS = {
    messages.INFO: "",
    messages.ERROR: "danger",
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    'rest_framework.authtoken',
    'cart',
    'payment',
    'users',
    'services',
    'website',
    'django_quill',
    
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

ROOT_URLCONF = 'edutech_io.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'edutech_io.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_SETTING_NAME", default=True),
        'USER': os.getenv("DB_SETTING_USER", default=True),
        'PASSWORD': os.getenv("DB_SETTING_PASSWORD", default=True),
        'HOST': os.getenv("DB_SETTING_HOST", default=True),
        'PORT': os.getenv("DB_SETTING_PORT", default=True)
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'users.User'

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, "edutech_io/static/")

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static/"),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Celery settings
CELERY_BROKER_URL = os.getenv("CELERY_SITTING_BROKER_URL", default=''), 
CELERY_RESULT_BACKEND = os.getenv("CELERY_SITTING_RESULT_BACKEND", default=''), 
CELERY_TIMEZONE = os.getenv("CELERY_SITTING_TIMEZONE", default=''), 

# Load Celery tasks from all registered apps
CELERY_IMPORTS = (
    '',
)

# EMAIL_BACKEND =  os.getenv("EMAIL_SETTING_BACKEND", default=''), 
# EMAIL_HOST =  os.getenv("EMAIL_SETTING_HOST", default=''), 
# EMAIL_USE_TLS =  os.getenv("EMAIL_SETTING_USE_TLS", default=''), 
# EMAIL_PORT =  os.getenv("EMAIL_SETTING_PORT", default=''), 
# EMAIL_HOST_USER =  os.getenv("EMAIL_SETTING_HOST_USER", default=''), 
# EMAIL_HOST_PASSWORD =  os.getenv("EMAIL_SETTING_HOST_PASSWORD", default=''), 