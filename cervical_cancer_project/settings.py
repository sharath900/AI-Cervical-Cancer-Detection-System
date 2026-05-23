"""
Django settings for cervical_cancer_project project.
"""

from pathlib import Path
from dotenv import load_dotenv
import os

# LOAD ENV VARIABLES
load_dotenv()

# BASE DIRECTORY
BASE_DIR = Path(__file__).resolve().parent.parent


# =========================================================================
# SECURITY SETTINGS
# =========================================================================
SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['*']


# =========================================================================
# APPLICATIONS
# =========================================================================
INSTALLED_APPS = [

    'detector',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


# =========================================================================
# MIDDLEWARE
# =========================================================================
MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    # WHITENOISE
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# =========================================================================
# URLS
# =========================================================================
ROOT_URLCONF = 'cervical_cancer_project.urls'


# =========================================================================
# TEMPLATES
# =========================================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [BASE_DIR / 'templates'],

        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [

                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# =========================================================================
# WSGI
# =========================================================================
WSGI_APPLICATION = 'cervical_cancer_project.wsgi.application'


# =========================================================================
# DATABASE
# =========================================================================
DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql',

        'NAME': os.getenv('DB_NAME'),

        'USER': os.getenv('DB_USER'),

        'PASSWORD': os.getenv('DB_PASSWORD'),

        'HOST': os.getenv('DB_HOST'),

        'PORT': os.getenv('DB_PORT'),
    }
}


# =========================================================================
# PASSWORD VALIDATION
# =========================================================================
AUTH_PASSWORD_VALIDATORS = [

    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# =========================================================================
# INTERNATIONALIZATION
# =========================================================================
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# =========================================================================
# STATIC FILES
# =========================================================================
STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'


# =========================================================================
# MEDIA FILES
# =========================================================================
MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'


# =========================================================================
# LOGIN SETTINGS
# =========================================================================
LOGIN_URL = 'login'

LOGIN_REDIRECT_URL = 'home'


# =========================================================================
# DEFAULT PRIMARY KEY
# =========================================================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'